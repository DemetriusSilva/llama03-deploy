FROM python:3.9-slim

RUN apt-get update && apt-get install -y curl nginx

# Instale o Ollama
RUN curl https://ollama.ai/install.sh | sh

# Configure o diretório de trabalho
WORKDIR /app

# Copie os arquivos necessários
COPY requirements.txt .
COPY index.html .
COPY nginx.conf /etc/nginx/sites-available/default

# Instale as dependências Python
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copie o resto dos arquivos
COPY . .

# Configure o Nginx
RUN rm -f /etc/nginx/sites-enabled/default && \
    ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/

# Verifique se o index.html foi copiado corretamente
RUN ls -l /app && cat /app/index.html

# Exponha a porta 80 para o Nginx
EXPOSE 80

# Disk
VOLUME /var/lib/ollama

# Comando para iniciar o Nginx, Ollama e a aplicação Flask
CMD service nginx start && ollama serve & python app.py
