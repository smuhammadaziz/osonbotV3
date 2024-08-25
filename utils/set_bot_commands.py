from aiogram import Bot
from aiogram.methods import SetMyCommands
from aiogram.types import BotCommand, BotCommandScopeAllPrivateChats, BotCommandScopeAllGroupChats

from typing import NoReturn

async def set_default_commands(bot: Bot) -> NoReturn:
    commands = [
        BotCommand(command="/start", description="START BOT"),
    ]

    group_commands = [
        BotCommand(command="/show", description="Admin Panel")
    ]
    await bot.set_my_commands(commands=commands, scope=BotCommandScopeAllPrivateChats())

    await bot.set_my_commands(commands=group_commands, scope=BotCommandScopeAllGroupChats())
