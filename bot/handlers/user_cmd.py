from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Приветик {message.from_user.first_name}")
