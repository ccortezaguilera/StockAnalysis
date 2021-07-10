import ujson
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from stockanalysis.core.config import settings

engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URI,
    pool_pre_ping=True,
    hide_parameters=settings.ENVIRONMENT != "dev",
    json_deserializer=ujson.loads,
    json_serializer=ujson.dumps,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
