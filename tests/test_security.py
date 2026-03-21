from http import HTTPStatus

from jwt import decode

from fast_zero.security import create_access_token


def test_jwt(settings):
    claim = {'test': 'test'}
    token = create_access_token(claim)

    decoded = decode(
        jwt=token, key=settings.SECRET_KEY, algorithms=settings.ALGORITHM
    )

    assert decoded['test'] == claim['test']
    assert 'exp' in decoded


def test_jwt_invalid_token(client):
    response = client.delete(
        '/users/1', headers={'Authorization': 'Bearer invalid token'}
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Could not validate credentials'}
