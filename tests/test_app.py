from http import HTTPStatus


def test_root_deve_retornar_ola_mundo(client):
    response = client.get('/')

    assert response.json() == {'Message': 'Hello World'}


def test_root_deve_retornar_html(client):
    response = client.get('/html')

    assert (
        response.text
        == """
    <html>
    <body>
    <h1>Olá Mundo</h1>
    </body>
    </html>
"""
    )


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'email': 'alice@example.com',
        'username': 'alice',
    }


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'id': 1,
                'email': 'alice@example.com',
                'username': 'alice',
            },
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'email': 'gabriel@example.com',
            'username': 'gabriel',
            'password': '123456',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'email': 'gabriel@example.com',
        'username': 'gabriel',
    }


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'email': 'gabriel@example.com',
        'username': 'gabriel',
    }
