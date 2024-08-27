from flask import Flask, send_file, request, jsonify
import requests
import os

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def serve_ui():
    index_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'index.html')
    app.logger.info(f"Attempting to serve index.html from: {index_path}")
    if os.path.exists(index_path):
        return send_file(index_path)
    else:
        app.logger.error(f"index.html not found at: {index_path}")
        return "Error: index.html not found", 404

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    prompt = data.get('prompt')
    response = requests.post('http://localhost:11434/api/generate', json={
        "model": "llama2",
        "prompt": prompt
    })
    return jsonify({"response": response.json()['response']})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
