from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

router = Router()


@router.message(CommandStart()) #? Команда старта
async def start(message: Message):
    await message.answer(f"Приветик {message.from_user.first_name}")

    
@router.message(Command("help")) #? Команда помощи
async def help(message: Message):
    await message.answer("Это помощь по боту)")
