# from typing import Any

from sqlalchemy import BigInteger, Column, DateTime
from sqlalchemy.dialects import sqlite
from sqlalchemy.ext.declarative import as_declarative, declared_attr

from stockanalysis.db.stub import utcnow

BigIntegerType = BigInteger().with_variant(sqlite.INTEGER(), "sqlite")


@as_declarative()
class Base:
    __name__: str
    created_at = Column(
        DateTime, default=utcnow(), nullable=False, server_default=utcnow()
    )
    modified_at = Column(DateTime, default=utcnow(), onupdate=utcnow(), nullable=False)

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
