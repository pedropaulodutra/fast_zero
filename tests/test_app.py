from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_must_return_200():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK


def test_home_should_return_hello_world():
    client = TestClient(app)

    response = client.get('/home')
    assert response.status_code == HTTPStatus.OK
    assert 'Hello World!' in response.text
