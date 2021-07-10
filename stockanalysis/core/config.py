import os
from typing import Any, Optional

from pydantic import BaseSettings  # AnyUrl

DEV_FILE = ".env"
STAGE_FILE = "stage.env"
PROD_FILE = "prod.env"

env_base_path = os.path.join(os.path.dirname(__file__), "..", "..")

dev_path = os.path.abspath(os.path.join(env_base_path, DEV_FILE))
stage_path = os.path.abspath(os.path.join(env_base_path, STAGE_FILE))  # noqa
prod_path = os.path.abspath(os.path.join(env_base_path, PROD_FILE))  # noqa


ENV_CONFIG_MAPPING = {
    "dev": dev_path,
    "stage": stage_path,
    "prod": prod_path,
}


env = os.getenv("ENV", "dev")


class Settings(BaseSettings):
    API_V1_STR: str
    ENVIRONMENT: str
    SQLALCHEMY_DATABASE_URI: Optional[Any] = None

    class Config:
        case_sensitive = True
        env_file_encoding = "utf-8"


settings = Settings(_env_file=ENV_CONFIG_MAPPING.get(env))
