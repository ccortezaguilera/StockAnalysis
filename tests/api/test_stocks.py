import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from stockanalysis.core.config import settings
from stockanalysis.models.stock import Stock


def test_read_stocks(client: TestClient, db: Session) -> None:
    ticker = "testing"
    db_obj = Stock(ticker=ticker)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    response = client.get(
        f"{settings.API_V1_STR}/stocks/{ticker}",
    )
    assert response.status_code == 200
    # content = response.json()


@pytest.mark.xfail(reason="TODO")
def test_create_stocks(client: TestClient, db: Session) -> None:
    pass
