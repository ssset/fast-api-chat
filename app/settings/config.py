from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    mongodb_connection_url: str = Field(alias='MONGO_DB_CONNECTION_URL')
    mongodb_chat_database: str = Field(default='chat', alias='MONGODB_CHAT_DATABASE')
    mongodb_chat_collection: str = Field(default='chat', alias='MONGODB_CHAT_COLLECTION')

    model_config = SettingsConfigDict(
        env_file='.env',
        extra='ignore'
    )