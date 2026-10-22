from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class DatabaseConfig(BaseSettings):
    db_uri: str = Field(validation_alias="MONGO_URI")
    db_name: str = Field(validation_alias="MONGO_DB_NAME")

    model_config = SettingsConfigDict(extra="ignore", env_file=".env", env_file_encoding="utf-8", populate_by_name=True)

@lru_cache
def get_database_config() -> DatabaseConfig:
    return DatabaseConfig()
