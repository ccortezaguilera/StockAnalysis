import ujson
from humps import camelize
from pydantic import BaseModel


class CamelCasedBase(BaseModel):
    class Config:
        alias_generator = camelize
        allow_population_by_field_name = True


class Base(CamelCasedBase):
    class Config(CamelCasedBase.Config):
        json_loads = ujson.loads
        json_dumps = ujson.dumps
