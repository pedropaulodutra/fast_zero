import sqlalchemy as sa
from sqlalchemy.orm import Session

from fast_zero.settings import Settings

engine = sa.create_engine(Settings().DATABASE_URL)


def get_session():
    with Session(engine) as session:
        yield session
