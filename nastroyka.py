import os
from pydantic import SecretStr, BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    bot_token: SecretStr
    ADMIN_CHAT_ID: int
    model_config: SettingsConfigDict = SettingsConfigDict(

        env_file = '.env',
        env_file_encoding = 'utf-8'
    )

config = Settings()