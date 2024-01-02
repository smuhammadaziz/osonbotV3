from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart

from keyboards.inline.HomeButton import start_button, allRegionsKvartira

from aiogram.fsm.context import FSMContext

from aiogram.types.callback_query import CallbackQuery
from aiogram.fsm.state import any_state

from loader import bot

from keyboards.inline.data import StartData

user_router = Router()

@user_router.message(CommandStart())
async def bot_start(message: Message):
    pinned_message = await message.answer(text="ЭЪЛОН БЕРИШ", reply_markup=start_button)

    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)

    await bot.pin_chat_message(chat_id=message.chat.id, message_id=pinned_message.message_id)

    await message.answer("<b> Ҳудудни танланг:  </b>", reply_markup=allRegionsKvartira, parse_mode="HTML")


@user_router.callback_query(StartData.filter(F.word=="start"), any_state)
async def starter_bot(call: CallbackQuery, state: FSMContext, callback_data: StartData):
    await call.answer("Bot ishga tushdi")
    await state.clear()
    await call.message.answer("<b> Ҳудудни танланг:  </b>", reply_markup=allRegionsKvartira, parse_mode="HTML")


@user_router.message(F.text=="START", any_state)
async def first(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("<b> Ҳудудни танланг:  </b>", reply_markup=allRegionsKvartira, parse_mode="HTML")


@user_router.message(F.text=="start", any_state)
async def first(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("<b> Ҳудудни танланг:  </b>", reply_markup=allRegionsKvartira, parse_mode="HTML")


@user_router.message(F.text=="/start", any_state)
async def first(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("<b> Ҳудудни танланг:  </b>", reply_markup=allRegionsKvartira, parse_mode="HTML")


@user_router.message(F.text=="/stop", any_state)
async def stop(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Bot is stopping", reply_markup=allRegionsKvartira, parse_mode="HTML")

@user_router.message(F.text=="/restart", any_state)
async def restart(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("<b> Ҳудудни танланг:  </b>", reply_markup=allRegionsKvartira, parse_mode="HTML")

@user_router.message(F.text=="⬅️ Ортга")
async def ortga(message: Message):
    await message.answer("<b> Ҳудудни танланг: </b>", reply_markup=allRegionsKvartira, parse_mode="HTML")

@user_router.callback_query(F.text=="hometypeortgabutton")
async def kvartirasotish(call: CallbackQuery):
    await call.answer("Категорияни танланг")
    await call.message.answer("<b> Ҳудудни танланг:  </b>", reply_markup=allRegionsKvartira, parse_mode="HTML")
