FROM python:3.9-slim

RUN apt-get update && apt-get install -y curl nginx

# Instale o Ollama
RUN curl https://ollama.ai/install.sh | sh

# Configure o diretório de trabalho
WORKDIR /app

# Copie os arquivos necessários
COPY . .

# Atualize pip e instale as dependências Python
RUN pip3 install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt

# Configure o Nginx
COPY nginx.conf /etc/nginx/sites-available/default
RUN ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/

# Exponha a porta 80 para o Nginx
EXPOSE 80

# Disk
VOLUME /var/lib/ollama

# Comando para iniciar o Nginx, Ollama e a aplicação Flask
CMD service nginx start && ollama serve & python3 app.py
