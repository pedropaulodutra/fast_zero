from contextlib import contextmanager

import pytest
import sqlalchemy as sa
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from fast_zero.app import app
from fast_zero.models import Base


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def session():
    engine = sa.create_engine('sqlite:///:memory:')

    Base.metadata.create_all(engine)

    with Session(engine) as session:
        yield session

    Base.metadata.drop_all(engine)


@contextmanager
def _mock_db_time(*, model, time):
    def fake_time_hook(mapper, connection, target):
        if hasattr(target, 'created_at'):
            target.created_at = time
        if hasattr(target, 'updated_at'):
            target.updated_at = time

    sa.event.listen(model, 'before_insert', fake_time_hook)
    yield time
    sa.event.remove(model, 'before_insert', fake_time_hook)


@pytest.fixture
def mock_db_time():
    return _mock_db_time
