FROM python:3.9-slim

RUN apt-get update && apt-get install -y curl nginx

# Instale o Ollama
RUN curl https://ollama.ai/install.sh | sh

# Configure o diretório de trabalho
WORKDIR /app

# Copie os arquivos necessários
COPY requirements.txt .

# Instale as dependências Python
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copie o resto dos arquivos
COPY . .

# Configure o Nginx
COPY nginx.conf /etc/nginx/sites-available/default
RUN rm -f /etc/nginx/sites-enabled/default && \
    ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/

# Exponha a porta 80 para o Nginx
EXPOSE 80

# Disk
VOLUME /var/lib/ollama

# Comando para iniciar o Nginx, Ollama e a aplicação Flask
CMD service nginx start && ollama serve & python -m flask run --host=0.0.0.0 --port=5000
