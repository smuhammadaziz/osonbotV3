from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from utils.db.postgres import Database

import config

storage = MemoryStorage()

dp = Dispatcher(storage=storage)

db = Database()


bot = Bot(token=config.BOT_TOKEN, parse_mode="HTML")

