from fastapi.testclient import TestClient

from fastapi_zero.app import app


def test_root_deve_retornar_ola_mundo():
    client = TestClient(app)

    response = client.get('/')

    assert response.json() == {'Message': 'Hello World'}


def test_root_deve_retornar_html():
    client = TestClient(app)

    response = client.get('/html')

    assert response.text == """
    <html>
    <body>
    <h1>Olá Mundo</h1>
    </body>
    </html>
"""
