from flask import Flask, request, jsonify, send_from_directory
import requests

app = Flask(__name__)

@app.route('/')
def serve_ui():
    return send_from_directory('.', 'index.html')

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
