# Ollama com Interface Web no Render

Este projeto configura o Ollama para ser executado como um serviço web no Render.com, incluindo uma interface web para interação.

## Como usar

1. Fork este repositório
2. Configure um novo serviço web no Render.com usando este repositório
3. No Render, defina a porta do serviço como 80
4. Deploy e acesse a URL fornecida pelo Render para usar a interface web do Ollama

## Estrutura do Projeto

- `app.py`: Aplicação Flask que serve como proxy para o Ollama
- `index.html`: Interface web para interagir com o Ollama
- `Dockerfile`: Configuração para criar a imagem Docker
- `nginx.conf`: Configuração do Nginx para servir a aplicação web e a API
- `requirements.txt`: Dependências Python necessárias

## Desenvolvimento Local

Para executar este projeto localmente:

1. Instale o Docker
2. Construa a imagem: `docker build -t ollama-web .`
3. Execute o container: `docker run -p 80:80 ollama-web`
4. Acesse `http://localhost` no seu navegador
