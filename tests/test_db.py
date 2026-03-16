from dataclasses import asdict
from datetime import datetime

import sqlalchemy as sa

from fast_zero.models import User


def test_create_user(session, mock_db_time):
    with mock_db_time(model=User, time=datetime.now()) as time:
        new_user = User(
            username='pedrodutra',
            email='pedrodutra86@hotmail.com',
            password='1234',
        )

        session.add(new_user)
        session.commit()

        user = session.scalar(
            sa.select(User).where(User.username == 'pedrodutra')
        )

    assert asdict(user) == {
        'id': 1,
        'username': 'pedrodutra',
        'email': 'pedrodutra86@hotmail.com',
        'password': '1234',
        'created_at': time,
        'updated_at': time
    }
