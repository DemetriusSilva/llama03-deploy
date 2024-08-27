from flask import Flask, send_from_directory, request, jsonify
import requests
import os
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
@app.route('/index.html')
def serve_ui():
    app.logger.info("Attempting to serve index.html")
    try:
        return send_from_directory(os.path.dirname(os.path.abspath(__file__)), 'index.html')
    except Exception as e:
        app.logger.error(f"Error serving index.html: {str(e)}")
        return f"Error serving UI: {str(e)}", 500

@app.route('/api/chat', methods=['POST'])
def chat():
    app.logger.info("Received chat request")
    try:
        data = request.json
        prompt = data.get('prompt')
        response = requests.post('http://localhost:11434/api/generate', json={
            "model": "llama2",
            "prompt": prompt
        })
        return jsonify({"response": response.json()['response']})
    except Exception as e:
        app.logger.error(f"Error in chat endpoint: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
