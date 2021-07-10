from typing import Generator  # Dict,

import pytest
from fastapi.testclient import TestClient

from stockanalysis.app import app
from stockanalysis.db.session import SessionLocal


@pytest.fixture(scope="session")
def db() -> Generator:
    yield SessionLocal()


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c
