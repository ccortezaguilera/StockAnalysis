from sqlalchemy import Column, DateTime, Float, ForeignKey, Sequence, String
from sqlalchemy.orm import relationship

from stockanalysis.db.base_class import Base, BigIntegerType


class Stock(Base):
    ticker = Column(String(10), primary_key=True)
    stock_days = relationship("StockDay", back_populates="stocks")

    def __repr__(self):
        return f"<Stock {self.ticker}>"


class StockDay(Base):
    id = Column(
        BigIntegerType,
        Sequence("id_seq"),
        primary_key=True,
        autoincrement=True,
        unique=True,
    )
    close = Column(Float)
    date = Column(DateTime)
    high = Column(Float)
    low = Column(Float)
    open = Column(Float)
    volume = Column(BigIntegerType)

    stock_id = Column(String(10), ForeignKey("stock.ticker"))
    stocks = relationship("Stock", foreign_keys=[stock_id], back_populates="stock_days")

    def __repr__(self):
        return f"<StockDay {self.date} {self.stock_id}>"
