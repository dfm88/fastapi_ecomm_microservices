import os
from functools import lru_cache
from typing import Any, Dict, Optional

from dotenv import load_dotenv
from pydantic import AnyHttpUrl, BaseSettings, PostgresDsn, validator

load_dotenv()


class BaseConfig(BaseSettings):
    API_V1_STR: str = os.environ.get('API_V1_STR')
    PROJECT_NAME: str = os.environ.get('PROJECT_NAME')

    JWT_SECRET_KEY: str = os.environ.get('JWT_SECRET_KEY')
    JWT_SECRET_KEY_REFRESH: str = os.environ.get('JWT_SECRET_KEY_REFRESH')

    ALGORITHM = os.environ.get('ALGORITHM')
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days

    BACKEND_CORS_ORIGINS: str | list[AnyHttpUrl] = os.environ.get(
        'BACKEND_CORS_ORIGINS', 'http://localhost:3000,http://localhost:8000'
    )

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: str | list[str]) -> str | list[str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)
    
    SQLALCHEMY_DATABASE_URI: str = os.environ.get('SQLALCHEMY_DATABASE_URI')

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if v is None:
            raise ValueError(v)
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    class Config:
        case_sensitive = True


class DevelopmentConfig(BaseConfig):
    LOGGING_LEVEL = 'DEBUG'


class ProductionConfig(BaseConfig):
    LOGGING_LEVEL = 'INFO'


class TestingConfig(BaseConfig):
    # define new attributes with respect to BaseConfig
    DATABASE_CONNECT_DICT: dict = {"check_same_thread": False}
    LOGGING_LEVEL = 'DEBUG'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # override attributes of BaseConfig
        # https://fastapi.tiangolo.com/advanced/testing-database/
        self.SQLALCHEMY_DATABASE_URI: str = "sqlite:///./test.db"


@lru_cache()
def get_settings():
    config_cls_dict = {
        "development": DevelopmentConfig,
        "production": ProductionConfig,
        "testing": TestingConfig,
    }

    config_name = os.environ.get("FASTAPI_CONFIG", "development")
    print('Running app in **%s** mode' % config_name)
    config_cls = config_cls_dict[config_name]
    return config_cls()


settings = get_settings()
