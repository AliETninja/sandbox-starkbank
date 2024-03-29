import logging
from pydantic import BaseSettings, PostgresDsn, RedisDsn


class Settings(BaseSettings):
    # API
    API_PREFIX: str = "/api/v1"
    API_VERSION: str = "0.1.0"

    # APP
    DEBUG: str = False
    APP_NAME: str = "Sandbox Starkbank"
    APP_DESCRIPTION: str = "Integração Sandbox para gerenciamento de fatura."

    # CELERY
    CELERY_APP_NAME: str = "worker"
    CELERY_BROKER_URL: RedisDsn
    CELERY_RESULT_BACKEND: RedisDsn

    # DATABASE
    DB_URI: PostgresDsn

    # STARKBANK
    SB_API_URL: str = "https://sandbox.api.starkbank.com/v2"
    SB_PROJECT_ID: str
    PRIVATE_KEY: str

    # GERADOR BRASILEIRO
    GB_API_URL: str = "https://geradorbrasileiro.com/api/faker"

    class Config:
        case_sensitive = True
        env_file = ".env.dev"
        env_file_encoding = "utf-8"


log = logging.getLogger("uvicorn")
log.info("Loading config settings from the environment...")
settings = Settings()
