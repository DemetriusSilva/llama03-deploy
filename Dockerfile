# Usar uma imagem base Python
FROM python:3.10-slim

# Definir o diretório de trabalho
WORKDIR /app

# Copiar os requisitos do projeto
COPY requirements.txt

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código do projeto
COPY . .

# Comando para rodar o Llama 03
CMD ["python", "app.py"]
