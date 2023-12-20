from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from filters.is_admins import Is_Admin_Group
from filters.chat_type import ChatTypeFilter

ban_unban_router = Router()


@ban_unban_router.message(Command("ban"), F.reply_to_message, Is_Admin_Group())
async def ban(message: Message):
    await message.chat.ban(user_id=message.reply_to_message.from_user.id)
    await message.answer(f"{message.reply_to_message.from_user.first_name} был заблокирован администратором {message.from_user.first_name}")
