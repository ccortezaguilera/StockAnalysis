from typing import Any, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from stockanalysis import schemas
from stockanalysis.api import deps
from stockanalysis.crud.crud_stock_days import stock_day

router = APIRouter()


@router.get("/", response_model=List[schemas.StockDay])
def read_stock_day(
    db: Session = Depends(deps.get_db), skip: int = 0, limit: int = 10
) -> Any:
    return stock_day.list(db, skip, limit)


@router.post("/", response_model=schemas.StockDay)
def create_stock_day(
    stock_day: schemas.StockDayCreate, db: Session = Depends(deps.get_db)
) -> Any:
    pass


@router.get("/status")
def status():
    return {"status": "ok"}
