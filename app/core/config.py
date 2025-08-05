from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', extra='ignore')

    DATABASE_URL: str
    SERVER_PORT: int = 8000
    DEBUG: bool = True

@lru_cache
def get_settings():
    return Settings()