from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fastapi_zero.schemas import Message

app = FastAPI(title='Minha API')


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'Message': 'Hello World'}


@app.get('/html', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def read_html():
    return """
    <html>
    <body>
    <h1>Olá Mundo</h1>
    </body>
    </html>
"""
