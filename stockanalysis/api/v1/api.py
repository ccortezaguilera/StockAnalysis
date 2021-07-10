from fastapi import APIRouter

from stockanalysis.api.v1.endpoints import stock_days, stocks

api_router = APIRouter()
api_router.include_router(stocks.router, prefix="/stocks", tags=["stocks"])
api_router.include_router(stock_days.router, prefix="/days", tags=["stock_days"])
