import os
import aiofiles
import asyncio

from typing import Optional, List
from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

from ujson import loads
from aiogram.types import BotCommand

async def get_json(filename: str) -> list:
    path = f"bot/data/json/{filename}.json"
    if os.path.exists(path):
        async with aiofiles.open(path, "r", encoding="utf-8") as file:
            return loads(await file.read())
    return []

#TODO Настройки конфигурации
class Settings(BaseSettings):
    token: SecretStr
    admins: List[int]
    commands: List = [BotCommand(command=cmd[0], description=cmd[1]) for cmd in asyncio.run(get_json("my_commands"))]
    webhook_domain: Optional[str]
    webhook_path: Optional[str]
    web_host: Optional[str] = "0.0.0.0"
    web_port: Optional[int] = 8080
    custom_webhook_domain: Optional[str]
    custom_webhook_path: Optional[str]
    
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')



config = Settings()

