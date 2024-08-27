FROM python:3.9-slim

RUN apt-get update && apt-get install -y curl nginx && apt-get clean && rm -rf /var/lib/apt/lists/*

# Instale o Ollama
RUN curl https://ollama.ai/install.sh | sh

# Configure o diretório de trabalho
WORKDIR /app

# Copie os arquivos necessários
COPY requirements.txt .
COPY app.py .
COPY wsgi.py .
COPY nginx.conf /etc/nginx/sites-available/default

# Instale as dependências Python
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Configure o Nginx
RUN rm -f /etc/nginx/sites-enabled/default && \
    ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/

# Exponha as portas 80 para o Nginx e 11434 para o Ollama
EXPOSE 80 11434

# Disk
VOLUME /var/lib/ollama

# Comando para iniciar o Nginx, Ollama e a aplicação Flask com Gunicorn
CMD service nginx start && \
    ollama serve & \
    echo "Waiting for Ollama to start..." && \
    sleep 10 && \
    echo "Starting Flask app with Gunicorn..." && \
    gunicorn --bind 0.0.0.0:5000 wsgi:app --log-level debug
