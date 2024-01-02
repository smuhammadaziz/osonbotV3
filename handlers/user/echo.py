from aiogram import Router
from aiogram.types import Message

from loader import bot

echo_router = Router()



@echo_router.message()
async def bot_echo(message: Message):
    await message.answer(message.text)