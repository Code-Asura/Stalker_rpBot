import os
import aiofiles

from ujson import loads
from dotenv import load_dotenv
from typing import Optional
from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    token: SecretStr
    admins: int
    webhook_domain: Optional[str]
    webhook_path: Optional[str]
    web_host: Optional[str] = "0.0.0.0"
    web_port: Optional[int] = 8080
    custom_webhook: Optional[str]

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    @classmethod
    def get_json(filename: str) -> list:
        path = f"data/json/{filename}.json"
        
        if os.path.exists(path):
            with aiofiles.open(path, "r", encoding="utf-8") as file:
                return loads(file.read())
        return []

    @classmethod
    def set_admins() -> list:
        load_dotenv()

        admins_list = os.getenv("ADMINS").split(", ")
        admins = [int(adm) for adm in admins_list]
        return admins

config = Settings()
