from typing import Optional
from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

#TODO Настройки конфигурации
class Settings(BaseSettings):
    token: SecretStr
    admins: int
    webhook_domain: Optional[str]
    webhook_path: Optional[str]
    web_host: Optional[str] = "0.0.0.0"
    web_port: Optional[int] = 8080
    custom_webhook_domain: Optional[str]
    custom_webhook_path: Optional[str]
    
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')


config = Settings()
