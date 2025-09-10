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
    question = request.form.get('question', '')
    files = request.files.getlist('files')

    saved_files = []
    if files:
        for file in files:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            saved_files.append(file_path)

    # Process files into document chunks
    document_chunks = process_input_files_or_session({"files": saved_files})

    # Build prompt
    prompt = build_prompt(question, document_chunks)

    # Get answer from on-prem LLM
    result = get_llm_response(prompt)

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)