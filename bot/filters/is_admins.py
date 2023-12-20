from typing import List

from aiogram.filters import BaseFilter
from aiogram.types import Message, Update
from aiogram import Bot

class Is_Admin(BaseFilter):
    def __init__(self, user_ids: int | List[int]) -> None:
        self.user_ids = user_ids

    async def __call__(self, message: Message) -> bool:
        if isinstance(self.user_ids, int):
            return message.from_user.id == self.user_ids
        return message.from_user.id in self.user_ids


class Is_Admin_Group(BaseFilter):

    async def __call__(self, message: Message, bot: Bot) -> bool:
        member = await bot.get_chat_member(message.chat.id, message.from_user.id)
        if member == "ChatMemberOwner" or "ChatMemberAdministrator":
            return True
        else: 
            return False
