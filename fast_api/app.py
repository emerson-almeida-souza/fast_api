from http import HTTPStatus
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_api.shemas import Message

app = FastAPI()

@app.get('/', status_code=HTTPStatus.OK, response_model=Message) 
def read_root():
    return {'message': 'GET OLÁ MUNDO!'}

@app.get('/html', status_code=HTTPStatus.OK, response_class=HTMLResponse) 
def read_root():
    return """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Página HTML Simples</title>
    </head>
    <body>
        <h1>Bem-vindo à minha página!</h1>
        <p>Este é um exemplo de uma página HTML simples.</p>
        <a href="https://www.example.com" target="_blank">Visite o Example.com</a>
    </body>
    </html>"""

@app.post('/')
def read_root():
    return {'message': 'POST Olá Mundo!'}
