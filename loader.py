from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

import config

storage = MemoryStorage()

dp = Dispatcher(storage=storage)

bot = Bot(token=config.BOT_TOKEN, parse_mode="HTML")

