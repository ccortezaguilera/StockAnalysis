import logging
from typing import Any, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from stockanalysis import schemas  # models
from stockanalysis.api import deps
from stockanalysis.crud import stock as stocks

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/", response_model=schemas.ListStock)
def read_stocks(db: Session = Depends(deps.get_db)) -> Any:
    return {"stocks": stocks.list(db)}


@router.get("/{ticker}", response_model=schemas.Stock)
def read_stock(*, db: Session = Depends(deps.get_db), ticker: str) -> Any:
    return stocks.get_ticker(ticker)


@router.post("/{ticker}", response_model=schemas.StockDay)
def create_stock(
    ticker: str, stock_day: schemas.StockDayCreate, db: Session = Depends(deps.get_db)
) -> Any:
    return stocks.create(db, obj_in=stock_day, ticker=ticker)


@router.post("/search", response_model=List[schemas.Stock])
def search_stocks(search: schemas.StockSearch, db: Session = Depends(deps.get_db)):
    return stocks.filter(db, obj_in=search)


@router.get("/status")
def status():
    return {"status": "ok"}
