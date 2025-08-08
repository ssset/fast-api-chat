from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    mongodb_connection_url: str = Field(alias='MONGO_DB_CONNECTION_URL')
    mongodb_chat_database: str = Field(default='chat', alias='MONGODB_CHAT_DATABASE')
    mongodb_chat_collection: str = Field(default='chat', alias='MONGODB_CHAT_COLLECTION')
    mongo_db_messages_collection: str = Field(default='messages', alias='MONGO_DB_MESSAGES_COLLECTION')

    
    kafka_url: str = Field(alias='KAFKA_URL')
    new_message_received_topic: str = Field(default='new-messages')
    new_chats_event_topic: str = Field(default='new_chats_topic')
    
    chat_deleted_topic: str = Field(default='chat_deleted_topic')

    model_config = SettingsConfigDict(
        env_file='.env',
        extra='ignore'
    )