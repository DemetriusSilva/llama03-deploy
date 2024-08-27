from flask import Flask, request, jsonify, make_response
import requests

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def serve_ui():
    html_content = '''
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Chat com Ollama</title>
        <style>
            body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
            #chatbox { height: 300px; border: 1px solid #ccc; overflow-y: scroll; margin-bottom: 10px; padding: 10px; }
            #userInput { width: 70%; padding: 5px; }
            #sendButton { padding: 5px 10px; }
        </style>
    </head>
    <body>
        <h1>Chat com Ollama</h1>
        <div id="chatbox"></div>
        <input type="text" id="userInput" placeholder="Digite sua mensagem...">
        <button id="sendButton">Enviar</button>

        <script>
            const chatbox = document.getElementById('chatbox');
            const userInput = document.getElementById('userInput');
            const sendButton = document.getElementById('sendButton');

            sendButton.addEventListener('click', sendMessage);
            userInput.addEventListener('keypress', function(e) {
                if (e.key === 'Enter') {
                    sendMessage();
                }
            });

            function sendMessage() {
                const message = userInput.value;
                if (message.trim() === '') return;

                appendMessage('Você: ' + message);
                userInput.value = '';

                fetch('/api/chat', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ prompt: message }),
                })
                .then(response => response.json())
                .then(data => {
                    if (data.error) {
                        appendMessage('Erro: ' + data.error);
                    } else {
                        appendMessage('Ollama: ' + data.response);
                    }
                })
                .catch(error => {
                    console.error('Erro:', error);
                    appendMessage('Erro ao obter resposta. Por favor, tente novamente.');
                });
            }

            function appendMessage(message) {
                const messageElement = document.createElement('p');
                messageElement.textContent = message;
                chatbox.appendChild(messageElement);
                chatbox.scrollTop = chatbox.scrollHeight;
            }
        </script>
    </body>
    </html>
    '''
    return make_response(html_content)

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
