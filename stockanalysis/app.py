from quart import Quart, render_template, jsonify, request, url_for, redirect, json
from werkzeug.exceptions import HTTPException
from datetime import datetime

from stocks.utils.conversion_type import get_conversion_type

__author__ = "Carlos Aguilera"
__version__ = "1.0.0"

from logging.config import dictConfig

dictConfig(
    {
        "version": 1,
        "loggers": {
            "quart.app": {"level": "INFO",},
            "quart.serving": {"level": "INFO"},
        },
    }
)

app = Quart(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/")
async def main():
    return await render_template("index.html")


@app.route("/status")
async def status():
    return jsonify({"status": "ok"})


@app.route("/process", methods=["POST"])
async def process():
    # https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo
    return 'Processing'
    # form = await request.form
    # __convtype = form.get("convtype")
    # todo add form validation
    # 1) for date invested
    # 2) amount invested
    # 3) stock ticker
    # todo add client side validation
    # 1) for date invested
    # 2) amount invested
    # 3) stock ticker
    # __day_invested = form.get("date_invested")
    # if __day_invested:
    #     __day_invested = datetime.strptime(__day_invested, "%Y-%M-%d")
    # __amount_invested = form.get("amount_invested")
    # __stock = form.get("symbol")
    # action = get_conversion_type(__convtype)
    # app.logger.info("%s Action %s", __convtype, action)
    # return action(
    #     symbol=__stock, date_invested=__day_invested, amount_invested=__amount_invested
    # )


@app.route("/what_if", methods=["POST"])
async def what_if(symbol, data_invested, amount_invested, convtype):
    return "Calculating"


@app.route("/result", methods=["POST"])
async def result(convtype):
    return "result"


@app.route("/stocks", methods=["GET"])
async def stocks():
    return jsonify(
        {"stocks": [{"location": "/stocks/appl"}, {"location": "/stocks/sq"}]}
    )


@app.errorhandler(Exception)
async def handle_exception(e):
    if isinstance(e, HTTPException):
        response = e.get_response()
        response.data = json.dumps(
            {"code": e.code, "name": e.name, "description": e.description,}
        )
        response.content_type = "application/json"
        app.logger.error("HTTP Error 500")
        return response
    app.logger.error("Error 500")
    return await render_template("500_generic.html", e=e)


if __name__ == "__main__":
    app.run()
