from aiogram import Router, F, Bot, types
from aiogram.types import Message, ContentType
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.enums.parse_mode import ParseMode

from loader import db

from filters.group_chat import IsGroup, IsGroupCall
from loader import bot  # Make sure the bot instance is imported correctly

from keyboards.inline.data import Tasdiqlash, BekorQilish, Bloklash, XabarYozish

# Initialize the router
verify_router = Router()

@verify_router.callback_query(IsGroupCall(), Tasdiqlash.filter(F.word=="tasdiqlash"))
async def dokumentlar(call: types.CallbackQuery):

    data = await db.yer_get_one_user_data()

    chat_id = call.message.message_id
    await bot.forward_message(chat_id=-1001747207701, from_chat_id=-1002212226293, message_id=chat_id)

    data = call.data

    print(data)

    await bot.send_message(chat_id=data[4:],
                           text="✅ E'lon kanalga joylandi!")
