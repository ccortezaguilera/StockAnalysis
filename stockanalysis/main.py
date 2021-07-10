# import locale
import logging
import os

# from datetime import datetime
from logging.config import dictConfig

from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException, RequestValidationError
from fastapi.responses import JSONResponse  # HTMLResponse,

# from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.routing import Mount

from stockanalysis.api.v1.api import api_router
from stockanalysis.core.config import settings
from stockanalysis.utils.helpers import checker as _

__author__ = "Carlos Aguilera"
__version__ = "1.0.0"


dictConfig(
    {
        "version": 1,
        "loggers": {
            "quart.app": {
                "level": "DEBUG",
            },
            "quart.serving": {"level": "DEBUG"},
            "stocks.stocks": {"level": "INFO"},
            "stockanalysis.api.v1.endpoints.stocks": {"level": "INFO"},
            "stockanalysis.app": {"level": "INFO"},
            "stockanalysis.crud.crud_stocks": {"level": "INFO"},
        },
    }
)
# logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Name, %s", __name__)

DB_NAME = os.path.join(os.path.dirname(__file__), "stocks.db")


# app.config["TEMPLATES_AUTO_RELOAD"] = True
# app.config["STOCKS_FOLDER"] = os.path.join(app.static_folder, "stocks")
TITLE = "Stock Analysis"
APP_ROOT_FOLDER = os.path.abspath(os.path.dirname(__file__))
TEMPLATE_FOLDER = os.path.join(APP_ROOT_FOLDER, "templates")
STATIC_FOLDER = os.path.join(APP_ROOT_FOLDER, "static")


sql_url = f"sqlite:///{DB_NAME}"

app = FastAPI(
    title=TITLE,
)

logger.info("Template location %s", TEMPLATE_FOLDER)
# No Static Route if it's in production
# app.mount("/static", StaticFiles(directory=STATIC_FOLDER), name="static")
templates = Jinja2Templates(directory=TEMPLATE_FOLDER)


app.include_router(api_router, prefix=f"/{settings.API_V1_STR}")


@app.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception):
    logger.exception(exc)
    return JSONResponse(status_code=404, content={"detail": "Not Found"})


@app.exception_handler(HTTPException)
async def http_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=404,
        content=jsonable_encoder(
            {
                "code": exc.code,
                "name": exc.name,
                "description": exc.description,
            }
        ),
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
    )


@app.on_event("startup")
async def startup_event():
    logger = logging.getLogger("uvicorn.access")
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    logger.addHandler(handler)


# todo swap for node root endpoint
# @app.get("/", response_class=HTMLResponse)
# async def root(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request})


@app.get("/status")
def get_status():
    return {"status": "ok"}


@app.get("/routes")
def get_routes():
    if settings.ENVIRONMENT == "production":
        return JSONResponse(status_code=404, content={"detail": "Not Found"})
    # routes = []
    routes_mapping = {}
    for route in sorted(app.routes, key=lambda r: r.path):
        if isinstance(route, Mount):
            _(routes_mapping, route.path, {"name": route.name})
        else:
            if settings.ENVIRONMENT == "dev":
                _(
                    routes_mapping,
                    route.path,
                    {"name": route.name, "methods": route.methods},
                )

            elif settings.ENVIRONMENT == "staging":
                _(routes_mapping, route.path, {})

    return {
        "routes": [{k: v} for k, v in routes_mapping.items()],
    }


@app.post("/what_if")
def what_if():
    pass


@app.post("/result")
def result():
    pass


# @app.errorhandler(Exception)
# async def handle_exception(e):
#     if isinstance(e, HTTPException):
#         response = e.get_response()
#         response.data = json.dumps(
#             {"code": e.code, "name": e.name, "description": e.description,}
#         )
#         response.content_type = "application/json"
#         app.logger.error("HTTP Error 500")
#         return response
#     app.logger.error(e)
#     return await render_template("500_generic.html", e=e)


# def create_app(config_obj):
#     app = Pint(
#       __name__,
#       title=TITLE,
#       template_folder=TEMPLATE_FOLDER,
#       static_folder=STATIC_FOLDER
#       )
#     app.config.update(config_obj)
#     with app.app_context():
#         for module in app.config.get('DB_MODELS_IMPORTS', list()):
#             import_module(module)


#     app.add_url_rule(
#        '/favicon.ico',
#       'favicon',
#       lambda: app.send_static_file('favicon.ico')
#       )
#     for bp in all_blueprints:
#         import_module(bp.import_name)
#         app.register_blueprint(bp)

#     db.init_app(app)

#     locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

#     ## Activate middleware
#     with app.app_context():
#         import_module('stockanalysis.middlewares')

#     return app


# if __name__ == "__main__":
# models_path = os.path.join(__file__, 'models')
# application = create_app({
#     'DB_MODELS_IMPORT': [
#         f
#         for f in os.listdir()
#         if os.path.isfile(os.path.join(models_path, f))
#     ],
# })
# application.run()
# app.run()
