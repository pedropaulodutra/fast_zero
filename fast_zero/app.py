from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_zero.schemas import Message

app = FastAPI(title='Task Manager')


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Hello World!'}


@app.get('/home', response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>Hello World!</title>
        </head>
        <body>
            <h1>Hello World!</h1>
        </body>
    </html>
"""
