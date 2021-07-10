import logging
import os
import sys
from http import HTTPStatus

import aiofiles
import yfinance as yf
from quart import jsonify, request, url_for
from quart_openapi import PintBlueprint, Resource

from stockanalysis.models.stock import StockDay  # Stock,

from .utils.extract_json_files import extract_json_file, generate_response
from .utils.query_params import (  # get_date_end,; get_date_start,
    get_max_results_size,
    get_page,
    get_page_size,
)

# from werkzeug.exceptions import BadRequest
# import datetime
# import json


# import stock_collection

logging.basicConfig(
    format="[%(asctime)s.%(msecs)03d] %(levelname)s:%(name)s: %(message)s",
    level=logging.DEBUG,
    datefmt="%Y-%m-%d %H:%M:%S",
    stream=sys.stderr,
)
logger = logging.getLogger(__name__)


def not_found():
    logger.error("Something happend!")
    return jsonify({"detail": "Not Found!"})


blueprint = PintBlueprint("stocks", __name__)
blueprint.register_error_handler(404, not_found)


DOWNLOAD = "download"
LIST = "list"
MAX_DAY_INCREASE = "max_day_increase"
REFRESH = "refresh"
# todo add constants


# def print_table(symbol, convtype):
#     collection = stock_collection.StockCollection()
#     collection.load()

#     if convtype == "list":
#         collection.list()

#     elif convtype == DOWNLOAD:
#         collection.download()

#     elif convtype == REFRESH:
#         collection.refresh()

#     elif convtype == MAX_DAY_INCREASE:
#         collection.max_day_increase(symbol)

#     elif convtype == "max_day_decrease":
#         collection.max_day_decrease(symbol)

#     elif convtype == "max_day_percent_increase":
#         collection.max_day_percent_increase(symbol)

#     elif convtype == "max_day_percent_decrease":
#         collection.max_day_percent_decrease(symbol)

#     elif convtype == "max_month_increase":
#         collection.max_month_increase(symbol)

#     elif convtype == "max_year_increase":
#         collection.max_year_increase(symbol)

#     elif convtype == "top3":
#         collection.top3()

#     else:
#         print("Command not recognized: %s for stock: %s" % (convtype, symbol))


# def print_a(symbol, date_invested, amount_invested, convtype):
#     collection = stock_collection.StockCollection()
#     collection.load()
#     if convtype == "what_if":
#         collection.what_if(symbol, date_invested, amount_invested, convtype)
#     else:
#         print(
#             "Command not recognized: %s %s %s %s"
#             % (symbol, date_invested, amount_invested, convtype)
#         )

all_schema = {
    "create": {"type": "string"},
    "read": {"type": "string"},
    "delete": {"type": "string"},
}


blueprint.create_validator(
    "symbol",
    {"type": "object", "properties": {"symbol": {"type": "string"}, **all_schema}},
)

stock_request = blueprint.create_validator(
    "stock", {"type": "object", "properties": {"symbol": {"type": "string"}}}
)


@blueprint.route("/stocks", methods=["GET", "POST"])
class Stocks(Resource):
    @blueprint.response(HTTPStatus.OK, description="Stocks endpoint")
    async def get(self):
        results = []
        # size = get_page_size(request)
        # page = get_page(request)
        # max_size = get_max_results_size(size, page)
        stocks_path = os.path.normcase(blueprint.stocks_folder)
        stocks = os.listdir(stocks_path)
        for filename in stocks:
            if filename.endswith(".json"):
                symbol_idx = filename.find(".json")
                symbol = filename[0:symbol_idx]
                results.append(
                    {
                        "symbol": symbol,
                        "info": url_for(
                            "stocks.get_media_for_stock_symbol", symbol=symbol
                        ),
                        "create": None,
                        "read": url_for(
                            "stocks.actions_for_stock_symbol", symbol=symbol
                        ),
                        "delete": None,
                    }
                )

        return jsonify({"create": url_for("stocks.stocks"), "results": results})

    @blueprint.expect(stock_request)
    @blueprint.response(HTTPStatus.OK, description="Stocks endpoint")
    @blueprint.response(HTTPStatus.BAD_REQUEST, "json response failure")
    async def post(self):
        data = await request.get_json()
        symbol = data["symbol"]
        stock = yf.Ticker(symbol)
        stock_data = stock.history(period="max")
        result = stock_data.to_json(orient="index", indent=4, date_format="iso")
        json_path = os.path.join(blueprint.stocks_folder, f"{symbol}.json")
        if os.path.exists(json_path):
            return {
                "symbol": symbol,
                "info": url_for("stocks.get_media_for_stock_symbol", symbol=symbol),
                "create": None,
                "read": url_for("stocks.actions_for_stock_symbol", symbol=symbol),
                "delete": None,
            }
        async with aiofiles.open(json_path, mode="w", newline="") as jsonfile:
            # todo fix the result keys to be corrected.
            # timestamp = datetime.datetime.fromisoformat(
            #    k.replace("Z", "+00:00")).strftime(
            #    "%Y-%m-%d"
            # )
            await jsonfile.write(result)
        return {
            "symbol": symbol,
            "info": url_for("stocks.get_media_for_stock_symbol", symbol=symbol),
            "create": None,
            "read": url_for("stocks.actions_for_stock_symbol", symbol=symbol),
            "delete": None,
        }


@blueprint.route("/stocks/<symbol>")
class GetMediaForStockSymbol(Resource):
    @blueprint.response(HTTPStatus.OK, description="Stock endpoint", validator="symbol")
    async def get(self, symbol):
        return jsonify(
            {
                "symbol": symbol,
                "create": None,
                "read": url_for("stocks.actions_for_stock_symbol", symbol=symbol),
                "delete": None,
            }
        )


@blueprint.route("/stocks/<symbol>/actions")
class ActionsForStockSymbol(Resource):
    async def get(self, symbol):
        return jsonify(
            {
                "historicalData": {
                    "read": url_for("stocks.historical_data_for_symbol", symbol=symbol),
                    "params": {
                        "date_start": "string:MM/DD/YY",
                        "date_end": "string:MM/DD/YY",
                        "size": "int",
                        "page": "int",
                    },
                }
            }
        )


@blueprint.route("/stocks/<symbol>/historical-data")
class HistoricalDataForSymbol(Resource):
    async def get(self, symbol):
        # date_start = get_date_start(request)
        # date_end = get_date_end(request)
        size = get_page_size(request)
        page = get_page(request)
        results = []
        max_size = get_max_results_size(size, page)
        stock_path = os.path.join(blueprint.stocks_folder, f"{symbol}.json")
        data = await extract_json_file(stock_path)
        for timestamp, content in generate_response(data, max_size):
            results.append(
                {
                    "date": timestamp,
                    "open": content["Open"],
                    "high": content["High"],
                    "low": content["Low"],
                    "close": content["Close"],
                    "volume": content["Volume"],
                }
            )

        return jsonify(
            {
                "historicalData": {
                    "read": url_for("stocks.historical_data_for_symbol", symbol=symbol),
                    "params": {
                        "date_start": "string:MM/DD/YY",
                        "date_end": "string:MM/DD/YY",
                        "size": "int",
                        "page": "int",
                    },
                },
                "results": results,
            }
        )


@blueprint.route("/stocks/<symbol>/history")
class StockHistory(Resource):
    async def get(self, symbol):
        stock_days = StockDay.query.order_by("date").paginate(
            0, per_page=25, error_out=False
        )
        stocks = []
        for stock_day in stock_days:
            # stock = Stock.query.get(id=stock_day.stock_id)
            stocks.append(
                {
                    # 'ticker': stock.ticker,
                    "close": stock_day.close,
                    "high": stock_day.high,
                }
            )
        return jsonify(
            {
                "stocks": stocks,
            }
        )


@blueprint.route("/status/stocks")
class StockStatus(Resource):
    @blueprint.response(
        HTTPStatus.OK, description="A status of ok is system is up.", validator="status"
    )
    async def get(self):
        return jsonify({"status": "ok"})


@blueprint.errorhandler(404)
async def handle_not_found(e):
    return jsonify({"detail": "Not Found"})
