# flake8: noqa
# Import all the models, so that Base has them before being
# imported by Alembic
from stockanalysis.db.base_class import Base
from stockanalysis.models.stock import Stock, StockDay
