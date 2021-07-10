from typing import List

from stockanalysis.schemas.base import Base


class StockBase(Base):
    ticker: str

    class Config(Base.Config):
        orm_mode = True


class StockCreate(StockBase):
    def __str__(self) -> str:
        return f"StockCreate {self.ticker}"


class Stock(StockBase):
    pass


class ListStock(Base):
    stocks: List[Stock]

    class Config(Base.Config):
        orm_mode = True


class StockSearch(Base):
    ticker: str
