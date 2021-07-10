from datetime import datetime

from stockanalysis.schemas.base import Base


class StockDayBase(Base):
    close: float
    date: datetime
    high: float
    low: float
    open: float
    volume: int


class StockDayInDBBase(StockDayBase):
    id: int
    stock_id: str

    class Config(Base.Config):
        orm_mode = True


class StockDay(StockDayInDBBase):
    pass


class StockDayCreate(StockDayBase):
    pass
