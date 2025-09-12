from flask import Flask, request, render_template, jsonify
import os
from chatbot_onprem import save_uploaded_files, process_input_files_or_session, build_prompt, get_llm_response

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    try:
        question = request.form.get('question', '').strip()
        print(f"Received question: {question}")
        if not question:
            return jsonify({"error": "Question is required"}), 400

        files = request.files.getlist('files')
        saved_files = []

        for file in files:
            if file and file.filename:
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                file.save(file_path)
                saved_files.append(file_path)

        print(f"Saved files: {saved_files}")

        input_parameters = {
            "question": question,
            "model": "llama3",
            "files": saved_files,
            "session_id": ""
        }

        document_chunks = process_input_files_or_session(input_parameters)
        print(f"Document chunks processed: {len(document_chunks)}")

        prompt = build_prompt(question, document_chunks)
        print(f"Built prompt: {prompt[:200]}...")  # print first 200 chars of prompt

        result = get_llm_response(prompt, model=input_parameters["model"])
        print(f"LLM Response Result: {result}")

        answer = result.get('answer') if isinstance(result, dict) else None
        if not answer:
            answer = "No answer returned."

        return jsonify({"answer": answer})

    except Exception as e:
        print(f"Exception in /ask: {e}")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

