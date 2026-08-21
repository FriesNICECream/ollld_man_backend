from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "ollld_man_backend"
    app_env: str = "development"
    database_url: str = (
        "postgresql+psycopg://ollld_man:ollld_man@localhost:5432/ollld_man"
    )

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
