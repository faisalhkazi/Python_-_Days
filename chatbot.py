import os
import shutil
from uuid import uuid4
import json
import re
import html
import requests

BASE_STORAGE_DIR = "./storage"
DOCUMENTS_DIR = os.path.join(BASE_STORAGE_DIR, "documents")
CHATS_DIR = os.path.join(BASE_STORAGE_DIR, "chats")

# Ensure base directories exist
os.makedirs(DOCUMENTS_DIR, exist_ok=True)
os.makedirs(CHATS_DIR, exist_ok=True)

def save_uploaded_files(file_paths):
    saved_files = []
    for file_path in file_paths:
        filename = os.path.basename(file_path)
        dest_path = os.path.join(DOCUMENTS_DIR, f"{uuid4()}_{filename}")
        shutil.copy(file_path, dest_path)  # Save to documents folder
        saved_files.append(dest_path)
    return saved_files

def get_session_chat_dir(session_id):
    session_dir = os.path.join(CHATS_DIR, session_id)
    os.makedirs(session_dir, exist_ok=True)
    return session_dir

def save_session_data(session_id, question, model, saved_files):
    session_dir = get_session_chat_dir(session_id)
    session_data = {
        "session_id": session_id,
        "question": question,
        "model": model,
        "files": saved_files
    }
    with open(os.path.join(session_dir, "session_data.json"), "w") as f:
        json.dump(session_data, f, indent=4)
    return session_data
    
def validate_input(input_parameters):
    # Check if 'question' is present and not empty
    if not input_parameters.get("question"):
        raise ValueError("Validation Error: 'question' parameter is required.")

    # Check if 'model' is present and not empty
    if not input_parameters.get("model"):
        raise ValueError("Validation Error: 'model' parameter is required.")

    # Check if at least one of 'files' or 'session_id' is provided
    files = input_parameters.get("files", [])
    session_id = input_parameters.get("session_id", "")

    if not files and not session_id:
        raise ValueError("Validation Error: At least one of 'files' or 'session_id' must be provided.")

    return True  # All validations passed
    
def process_input_files_or_session(input_parameters):
    session_id = input_parameters.get("session_id")
    files = input_parameters.get("files", [])

    if files:
        document_chunks = []

        for file_path in files:
            # 1️⃣ Extract text based on file type
            text = extract_text_from_file(file_path)

            # 2️⃣ Split text into chunks (for easier search later)
            chunks = split_text_into_chunks(text)

            document_chunks.extend(chunks)

        # Optionally: Store the document_chunks in session storage
        if session_id:
            store_chunks_for_session(session_id, document_chunks)

        return document_chunks

    elif session_id:
        # Retrieve previously stored document chunks
        document_chunks = retrieve_chunks_from_session(session_id)

        if not document_chunks:
            raise ValueError(f"No document chunks found for session_id: {session_id}")

        return document_chunks

    else:
        raise ValueError("No files or sessionId provided to process.")
        
def extract_text_from_file(file_path):
    if file_path.endswith(".pdf"):
        return extract_text_from_pdf(file_path)
    elif file_path.endswith(".docx") or file_path.endswith(".doc"):
        return extract_text_from_word(file_path)
    elif file_path.endswith(".xlsx") or file_path.endswith(".xls"):
        return extract_text_from_excel(file_path)
    else:
        raise ValueError(f"Unsupported file type: {file_path}")
        
def split_text_into_chunks(text, chunk_size=1000):
    # Simple example: Split by number of characters
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    
def store_chunks_for_session(session_id, document_chunks):
    session_dir = os.path.join(CHATS_DIR, session_id)
    os.makedirs(session_dir, exist_ok=True)
    with open(os.path.join(session_dir, "document_chunks.json"), "w") as f:
        json.dump(document_chunks, f, indent=4)

def retrieve_chunks_from_session(session_id):
    session_file = os.path.join(CHATS_DIR, session_id, "document_chunks.json")
    if os.path.exists(session_file):
        with open(session_file, "r") as f:
            return json.load(f)
    return None


def build_prompt(question, document_chunks):
    # Define a special test case pattern (example)
    test_case_pattern = r"(test case|unit test|example input|expected output)"

    if re.search(test_case_pattern, question, re.IGNORECASE):
        # Special Test Case Prompt Template
        prompt = f"""
You are a chatbot designed to help developers by providing test case examples.
Question: {question}
Please answer by generating a proper test case based on the input.
"""
    else:
        # Standard Prompt Template: Include document chunks and question
        documents_text = "\n\n---\n\n".join(document_chunks)
        prompt = f"""
You are a helpful assistant. Use the following documents to answer the question.

Documents:
{documents_text}

Question:
{question}

Answer:
"""

    return prompt
    
def get_llm_response(prompt, model="gpt-5-mini", api_url="http://localhost:11434/v1/completions"):
    """
    Sends prompt to the on-prem LLM and returns the response.
    
    Args:
        prompt (str): The prompt text.
        model (str): Model name to use.
        api_url (str): Local/on-prem API endpoint for completions.

    Returns:
        dict: JSON object containing the generated answer.
    """
    payload = {
        "model": model,
        "prompt": prompt,
        "max_tokens": 500,
        "temperature": 0.2
    }

    try:
        response = requests.post(api_url, json=payload)
        response.raise_for_status()
        data = response.json()
        
        # Extract the text output (depends on your on-prem model response format)
        # Adjust if your model returns something like: data['choices'][0]['text']
        answer_text = data.get("choices", [{}])[0].get("text", "")
        
        return {"answer": answer_text.strip()}
    
    except requests.exceptions.RequestException as e:
        return {"error": f"API request failed: {str(e)}"}

# Example usage
if __name__ == "__main__":
    # Build prompt (using your existing function)
    question = "Explain how the Python code handles document chunks."
    document_chunks = ["Chunk 1: ...", "Chunk 2: ..."]  # Example chunks
    prompt = build_prompt(question, document_chunks)
    
    # Call on-prem LLM
    result = get_llm_response(prompt, model="gpt-5-mini")
    
    # Print JSON response
    print(json.dumps(result, indent=4))
