"""Settings configuration"""
import os
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """Settings configuration"""
    model_config = SettingsConfigDict(env_file=".env")
    app_name: str = os.getenv(key="APP_NAME", default="Jarvis")

settings = Settings()
