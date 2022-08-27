from typing import Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from customers.main import app
from customers.api.deps.db import get_db
from customers.db.base_class import Base

from customers.core.config import TestingConfig

settings = TestingConfig()
print('test db uri', settings.SQLALCHEMY_DATABASE_URI)

engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URI,  # Sqlite test db
    connect_args=settings.DATABASE_CONNECT_DICT
)
TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture()
def db() -> Generator:
    # befrore each test create the db ...
    Base.metadata.create_all(bind=engine)
    yield TestingSessionLocal()
    # ... and drop it after
    # https://stackoverflow.com/questions/67255653/how-to-set-up-and-tear-down-a-database-between-tests-in-fastapi
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c


@pytest.fixture
def test_env(monkeypatch):
    monkeypatch.setenv("FASTAPI_CONFIG", "testing")
