from flask import Flask, render_template, request, jsonify
import requests
import os
import docx
from PyPDF2 import PdfReader

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

OLLAMA_API_URL = "http://localhost:11434/api/generate"   # Ollama endpoint
MODEL_NAME = "llama3"  # change this to your installed model: run `ollama list`

last_uploaded_file = None  # store last uploaded file path

# -------- Helper functions --------

def extract_text_from_file(filepath):
    """Extracts text from TXT, PDF, DOCX files."""
    ext = filepath.split(".")[-1].lower()
    text = ""

    if ext == "txt":
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            text = f.read()

    elif ext == "pdf":
        reader = PdfReader(filepath)
        for page in reader.pages:
            text += page.extract_text() + "\n"

    elif ext == "docx":
        doc = docx.Document(filepath)
        for para in doc.paragraphs:
            text += para.text + "\n"

    else:
        text = "Unsupported file format."

    return text.strip()

# -------- Routes --------

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"answer": "No file part in the request"}), 400
    
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"answer": "No selected file"}), 400

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    global last_uploaded_file
    last_uploaded_file = filepath

    return jsonify({"answer": f"File {file.filename} uploaded successfully."})

@app.route("/ask", methods=["POST"])
def ask_question():
    data = request.get_json()
    question = data.get("question", "")

    if not question:
        return jsonify({"answer": "Please enter a question"}), 400

    # If a file was uploaded, extract its text
    context = ""
    if last_uploaded_file:
        context = extract_text_from_file(last_uploaded_file)

    # Combine question with file context
    prompt = f"Answer the question based on this text:\n\n{context}\n\nQuestion: {question}"

    # Call Ollama
    try:
        response = requests.post(
            OLLAMA_API_URL,
            json={"model": MODEL_NAME, "prompt": prompt},
            stream=True
        )
        answer = ""
        for line in response.iter_lines():
            if line:
                data = line.decode("utf-8")
                if '"response":"' in data:
                    answer += data.split('"response":"')[1].split('"')[0]
    except Exception as e:
        return jsonify({"answer": f"Error: {str(e)}"})

    return jsonify({"answer": answer.strip() or "No response from model."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
