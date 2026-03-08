from http import HTTPStatus


def test_root_should_return_ok_and_hello_world(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello, World!'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'pedrodutra',
            'email': 'pedrodutra86@hotmail.com',
            'password': '1234',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'pedrodutra',
        'email': 'pedrodutra86@hotmail.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'pedrodutra',
                'email': 'pedrodutra86@hotmail.com',
                'id': 1,
            }
        ]
    }


def test_read_user(client):
    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'pedrodutra',
        'email': 'pedrodutra86@hotmail.com',
        'id': 1,
    }


def test_read_user_should_return_not_found(client):
    response = client.get('/users/2')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found.'}


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'kathleenvizani',
            'email': 'kathleencouto18@icloud.com',
            'password': '1234',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'kathleenvizani',
        'email': 'kathleencouto18@icloud.com',
        'id': 1,
    }


def test_update_user_should_return_not_found(client):
    response = client.put(
        '/users/2',
        json={
            'username': 'pedrodutra',
            'email': 'pedrodutra86@hotmail.com',
            'password': '1234',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found.'}


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'kathleenvizani',
        'email': 'kathleencouto18@icloud.com',
    }


def test_delete_user_should_return_not_found(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found.'}
