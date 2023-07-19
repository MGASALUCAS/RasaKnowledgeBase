from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_files():
    prompt_file = request.files['promptFile']
    document_files = request.files.getlist('documentFiles')

    # Move prompt.txt to the appropriate folder
    prompt_file.save(os.path.join('data', 'prompt.txt'))

    # Move external document files to the external_documents folder
    for document_file in document_files:
        document_file.save(os.path.join('external_documents', document_file.filename))

    return jsonify(success=True)

if __name__ == '__main__':
    app.run(debug=True)
