FROM ubuntu:latest

RUN apt-get update && apt-get install -y curl

# Instale o Ollama
RUN curl https://ollama.ai/install.sh | sh

# Configure o diretório de trabalho
WORKDIR /app

# Copie os arquivos necessários
COPY . .

# Exponha a porta 11434 (porta padrão do Ollama)
EXPOSE 11434

# Disk
VOLUME /var/lib/ollama

# Comando para iniciar o Ollama
CMD ollama serve
