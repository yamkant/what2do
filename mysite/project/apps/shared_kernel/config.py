import os
from pydantic_settings import BaseSettings

class Config(BaseSettings):
    ENV: str = "development"
    DEBUG: bool = True
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    WRITER_DB_URL: str = f"sqlite:///./sql_app.db"
    READER_DB_URL: str = f"sqlite:///./sql_app.db"
    JWT_SECRET_KEY: str = "4ab2fce7a6bd79e1c014396315ed322dd6edb1c5d975c6b74a2904135172c03c"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXIPRE_MINUTES: int = 60 * 24

class LocalConfig(Config):
    WRITER_DB_URL: str = f"sqlite:///./sql_app.db"
    READER_DB_URL: str = f"sqlite:///./sql_app.db"

class DevelopConfig(Config):
    WRITER_DB_URL: str = f"postgresql://postgres:postgres@localhost:5432/what2do"
    READER_DB_URL: str = f"postgresql://postgres:postgres@localhost:5432/what2do"

class ProductionConfig(Config):
    WRITER_DB_URL: str = f"postgresql://postgres:postgres@db:5432/what2do"
    READER_DB_URL: str = f"postgresql://postgres:postgres@db:5432/what2do"

def get_config():
    env = os.getenv("ENV", "local")
    config_type = {
        "local": LocalConfig(),
        "dev": DevelopConfig(),
        "prod": ProductionConfig(),
    }
    return config_type[env]

config: Config = get_config()