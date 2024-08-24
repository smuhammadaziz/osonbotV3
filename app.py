from handlers import register_handlers
from utils.set_bot_commands import set_default_commands
from aiogram import Dispatcher, Bot, Router
from aiogram.fsm.storage.memory import MemoryStorage

from loader import db


from asyncio import run
from pathlib import Path
from loguru import logger
from dotenv import load_dotenv

async def database_connected():
    # Ma'lumotlar bazasini yaratamiz:
    await db.create()
    # await db.drop_users()
    # await db.create_table_users()


async def main() -> None:
    base_dir = Path(__file__).resolve().parent.parent

    load_dotenv(base_dir / '.env')
    logger.add(base_dir / 'logs.log', level="INFO")

    import config

    dp: Dispatcher = Dispatcher(storage=MemoryStorage())
    bot = Bot(config.BOT_TOKEN)
    register_handlers(dp)

    

    logger.info('Bot started')
    await set_default_commands(bot)

    await database_connected()
    logger.info("Database connected")

    await dp.start_polling(bot)
    logger.info('Bot stopped')


if __name__ == '__main__':
    run(main())
