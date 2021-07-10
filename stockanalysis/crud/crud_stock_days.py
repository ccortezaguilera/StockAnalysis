from sqlalchemy.orm import Session

from stockanalysis.models.stock import StockDay
from stockanalysis.schemas import StockDayCreate


class CrudStockDay:
    def list(self, db: Session, skip: int = 0, limit: int = 45):
        return db.query(StockDay).offset(skip).limit(limit).all()

    def create_day(self, db: Session, *, obj_in: StockDayCreate):
        # todo figure out how to obtain the ticker
        obj_in_data = jsonable_encoder(obj_in)  # noqa: F821
        stock = self.get(db=db, ticker=ticker)  # noqa: F821
        if not stock:
            stock = self.create_ticker(db=db, ticker=ticker)  # noqa: F821
        db_obj = StockDay(**obj_in_data, ticker=ticker)  # noqa: F821
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        db_obj.stock_id = stock.ticker
        return db_obj


stock_day = CrudStockDay()
