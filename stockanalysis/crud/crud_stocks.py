import logging

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from stockanalysis.models.stock import Stock, StockDay
from stockanalysis.schemas.stock_days import StockDayCreate
from stockanalysis.schemas.stocks import StockCreate, StockSearch

logger = logging.getLogger(__name__)


class CrudStock:
    def get(self, db: Session, id: int):
        return db.query(Stock).get(id=id)

    def list(self, db: Session, skip: int = 0, limit: int = 45):
        return db.query(Stock).offset(skip).limit(limit).all()

    def get_ticker(self, db: Session, ticker: str):
        return db.query(Stock).get(ticker=ticker)

    def create_ticker(self, db: Session, *, obj_in: StockCreate) -> Stock:
        logging.warn(obj_in)
        obj_in_data = obj_in.dict()
        logging.warn(obj_in_data)
        db_obj = Stock(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        db.flush()
        return db_obj

    def create(self, db: Session, *, obj_in: StockDayCreate, ticker: str):
        obj_in_data = obj_in.dict()
        db_obj = StockDay(**obj_in_data, stock_id=ticker)
        stock = db.query(Stock).get(ticker)
        if not stock:
            stock = self.create_ticker(db=db, obj_in=StockCreate(ticker=ticker))
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        db.flush()
        return db_obj

    def filter(
        self, db: Session, *, obj_in: StockSearch, skip: int = 0, limit: int = 45
    ):
        obj_in_data = jsonable_encoder(obj_in)
        return db.query(Stock).filter_by(**obj_in_data).offset(skip).limit(limit).all()


stock = CrudStock()
