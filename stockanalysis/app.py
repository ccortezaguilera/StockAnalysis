import os
from http import HTTPStatus
from quart import render_template, jsonify, request, url_for, redirect, json
from quart_openapi import Pint, Resource
from werkzeug.exceptions import HTTPException
from datetime import datetime

# from stocks.utils.conversion_type import get_conversion_type

__author__ = "Carlos Aguilera"
__version__ = "1.0.0"

from logging.config import dictConfig
from stocks.stocks import blueprint

dictConfig(
    {
        "version": 1,
        "loggers": {
            "quart.app": {"level": "DEBUG",},
            "quart.serving": {"level": "DEBUG"},
            "stocks.stocks": {"level": "INFO"},
        },
    }
)

app = Pint(__name__, title="Stock Analysis")

app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["STOCKS_FOLDER"] = os.path.join(app.static_folder, "stocks")
blueprint.stocks_folder = os.path.join(app.static_folder, "stocks")

app.register_blueprint(blueprint)


@app.route("/", methods=["GET", "POST"], provide_automatic_options=False)
class Root(Resource):
    async def get(self):
        return await render_template("index.html")


status_expected_schema = app.create_validator(
    "status", {"type": "object", "properties": {"status": {"type": "string",},},}
)


@app.route("/status")
class Status(Resource):
    @app.response(
        HTTPStatus.OK,
        description="A status of ok is system is up.",
        validator=status_expected_schema,
    )
    async def get(self):
        return jsonify({"status": "ok"})


@app.route("/process", methods=["POST"])
class Process(Resource):
    async def post(self):
        return "Processing"
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
class WhatIf(Resource):
    async def post(self):
        return "Calculating"


@app.route("/result", methods=["POST"])
class Result(Resource):
    async def post(self):
        return "result"


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
    app.logger.error(e)
    return await render_template("500_generic.html", e=e)


if __name__ == "__main__":
    app.run()
