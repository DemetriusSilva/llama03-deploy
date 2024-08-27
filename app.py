from flask import Flask, request, jsonify, send_from_directory
import requests
import os
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def serve_ui():
    try:
        return send_from_directory(os.path.dirname(os.path.abspath(__file__)), 'index.html')
    except Exception as e:
        app.logger.error(f"Error serving index.html: {str(e)}")
        return "Error serving UI", 500

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
