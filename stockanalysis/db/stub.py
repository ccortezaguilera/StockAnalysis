from typing import Any

from sqlalchemy.ext.compiler import compiles
from sqlalchemy.sql import expression
from sqlalchemy.types import DateTime


class utcnow(expression.FunctionElement):
    type = DateTime()


# @compiles(utcnow, "postgresql")
# def pg_utcnow(element: Any, compiler: Any, **kw: Any):
#     return "TIMEZONE('utc', CURRENT_TIMESTAMP)"


@compiles(utcnow, "sqlite")
def pg_utcnow(element: Any, compiler: Any, **kw: Any):
    return "(DATETIME('NOW'))"
