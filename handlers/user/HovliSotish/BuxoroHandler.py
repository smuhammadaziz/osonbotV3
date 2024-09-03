import ast
from typing import List
from aiogram import types, F, Router
from aiogram.types import Message

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types.callback_query import CallbackQuery

from keyboards.default.JobButton import checkbtn, start
from keyboards.default.JobButton import otkazishButton
from keyboards.inline.HomeButton import remontButton, jihozlarButton, valyutaButton, borYoq
from keyboards.inline.HomeButton import buxoro_group

from loader import bot, db
from states.HovliState.BuxoroState import BuxoroHomeSotishHovli

from transliterate import to_cyrillic

from utils.QuestionHovli.hovliqs import hovlitanlandi, rasmlar, umumiyMaydonyoz, faqatRaqamyoz, gazyoz, \
    jihozlaryoz, kanalizatsiyayoz, manzilyoz, moljalyoz, narxiyoz, nechaQavatyoz,oshxonayoz, \
    qoshimchaMalumotyoz, remontyoz, suvyoz, svetyoz, telraqam1yoz, telraqam2yoz, valyutayoz, \
    xammomyoz, xonalaryoz, buxoro_id, check_text, buxororegion, data2, data32, data33, \
    data34, data35, success_text, group_id, success_message, fail_message


from keyboards.inline.data import BuxoroHovliData

from keyboards.inline.data import YoqData, BorData
from keyboards.inline.data import YevroremontData, TamirlangantData, OrtachaData, TamirsizData
from keyboards.inline.data import MavjudData, JihozlarsizData
from keyboards.inline.data import USDData, SUMData
from keyboards.inline.data import TasdiqlashBuxoro, BekorQilishBuxoro

mode = "Markdown"

from aiogram_media_group import media_group_handler
from utils.media_group import MediaGroupBuilder


from filters.group_chat import IsGroup, IsGroupCall


buxoro_router = Router()

@buxoro_router.callback_query(BuxoroHovliData.filter(F.word=="buxorohovli"))
async def first(callback_query: CallbackQuery, state: FSMContext, callback_data: BuxoroHovliData):
    # await callback_query.answer(hovlitanlandi)
    await callback_query.message.answer(rasmlar, parse_mode="HTML")

    await state.set_state(BuxoroHomeSotishHovli.images)


@buxoro_router.message(BuxoroHomeSotishHovli.images, F.media_group_id, F.content_type.in_({'photo'}))
@media_group_handler
async def album_handler(messages: List[types.Message], state: FSMContext):
    file_ids = []

    for message in messages:
        photos = message.photo

        first_photo_size = photos[0]
        first_file_id = first_photo_size.file_id

        file_ids.append(first_file_id)

    await state.update_data({
        "images": file_ids
    })

    await messages[-1].answer(umumiyMaydonyoz, parse_mode="HTML")
    await state.set_state(BuxoroHomeSotishHovli.umumiyMaydon)



@buxoro_router.message(lambda message: message.text and not message.text.replace('.', '').replace(',', '').isdigit(),
                    BuxoroHomeSotishHovli.umumiyMaydon)
async def check_umumiy(message: Message):
    await message.reply(faqatRaqamyoz)


@buxoro_router.message(BuxoroHomeSotishHovli.umumiyMaydon)
async def umumiymaydon(message: Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "umumiyMaydon": text
    })

    await state.set_state(BuxoroHomeSotishHovli.xonalar)

    await bot.send_message(chat_id=message.chat.id, text=xonalaryoz, parse_mode="HTML")


@buxoro_router.message(lambda message: message.text and not message.text.replace('.', '').replace(',', '').isdigit(),
                    BuxoroHomeSotishHovli.xonalar)
async def check_xonalar(message: Message):
    await message.reply(faqatRaqamyoz)


@buxoro_router.message(BuxoroHomeSotishHovli.xonalar)
async def umumiymaydon(message: Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "xonalar": text
    })

    await bot.send_message(chat_id=message.chat.id, text=oshxonayoz, parse_mode="HTML",
                           reply_markup=borYoq)
    await state.set_state(BuxoroHomeSotishHovli.oshxona)



# =================================================
@buxoro_router.callback_query(BorData.filter(F.word=="bor"), BuxoroHomeSotishHovli.oshxona)
async def kvartira(callback_query: CallbackQuery, state: FSMContext, callback_data: BorData):
    text = "бор"
    # await callback_query.answer("Pressed")

    await state.update_data({
        "oshxona": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=xammomyoz, reply_markup=borYoq, parse_mode="HTML")
    await state.set_state(BuxoroHomeSotishHovli.hammom)


@buxoro_router.callback_query(YoqData.filter(F.word=="yoq"), BuxoroHomeSotishHovli.oshxona)
async def kvartira(callback_query: CallbackQuery, state: FSMContext, callback_data: YoqData):
    text = "йўқ"
    # await callback_query.answer("Pressed")

    await state.update_data({
        "oshxona": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=xammomyoz, reply_markup=borYoq, parse_mode="HTML")
    await state.set_state(BuxoroHomeSotishHovli.hammom)


@buxoro_router.callback_query(BorData.filter(F.word=="bor"), BuxoroHomeSotishHovli.hammom)
async def kvartira(callback_query: CallbackQuery, state: FSMContext, callback_data: BorData):
    text = "бор"
    # await callback_query.answer("Pressed")

    await state.update_data({
        "hammom": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=nechaQavatyoz, parse_mode="HTML")
    await state.set_state(BuxoroHomeSotishHovli.qavat)


@buxoro_router.callback_query(YoqData.filter(F.word=="yoq"), BuxoroHomeSotishHovli.hammom)
async def kvartira(callback_query: CallbackQuery, state: FSMContext, callback_data: YoqData):
    text = "йўқ"
    # await callback_query.answer("Pressed")
    
    await state.update_data({
        "hammom": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=nechaQavatyoz, parse_mode="HTML")
    await state.set_state(BuxoroHomeSotishHovli.qavat)


# ==================================================================


@buxoro_router.message(lambda message: message.text and not message.text.replace('.', '').replace(',', '').isdigit(),
                    BuxoroHomeSotishHovli.qavat)
async def check_qavat(message: types.Message):
    await message.reply(faqatRaqamyoz)


@buxoro_router.message(BuxoroHomeSotishHovli.qavat)
async def umumiymaydon(message: types.Message, state: FSMContext):
    text = message.text

    await state.update_data({
        "qavat": text
    })

    await bot.send_message(chat_id=message.chat.id, text=remontyoz, parse_mode="HTML", 
                           reply_markup=remontButton)
    await state.set_state(BuxoroHomeSotishHovli.remont)


# ====================================================================
@buxoro_router.callback_query(YevroremontData.filter(F.word=="yevroremont"), BuxoroHomeSotishHovli.remont)
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext, callback_data: YevroremontData):
    text = "Евроремонт"
    # await callback_query.answer("Pressed")
    await state.update_data({
        "remont": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=jihozlaryoz,
                           reply_markup=jihozlarButton, parse_mode="HTML")
    await state.set_state(BuxoroHomeSotishHovli.jihozlar)


@buxoro_router.callback_query(TamirlangantData.filter(F.word=="tamirlangan"), BuxoroHomeSotishHovli.remont)
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext, callback_data: TamirlangantData):
    text = "Таъмирланган"
    # await callback_query.answer("Pressed")
    await state.update_data({
        "remont": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=jihozlaryoz,
                           reply_markup=jihozlarButton, parse_mode="HTML")
    await state.set_state(BuxoroHomeSotishHovli.jihozlar)


@buxoro_router.callback_query(OrtachaData.filter(F.word=="ortacha"), BuxoroHomeSotishHovli.remont)
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext, callback_data: OrtachaData):
    text = "Ўртача"
    # await callback_query.answer("Pressed")
    await state.update_data({
        "remont": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=jihozlaryoz,
                           reply_markup=jihozlarButton, parse_mode="HTML")
    await state.set_state(BuxoroHomeSotishHovli.jihozlar)


@buxoro_router.callback_query(TamirsizData.filter(F.word=="tamirsiz"), BuxoroHomeSotishHovli.remont)
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext, callback_data: TamirsizData):
    text = "Таъмирсиз"
    # await callback_query.answer("Pressed")
    await state.update_data({
        "remont": text
    })


    await bot.send_message(chat_id=callback_query.message.chat.id, text=jihozlaryoz,
                           reply_markup=jihozlarButton, parse_mode="HTML")
    await state.set_state(BuxoroHomeSotishHovli.jihozlar)


# ===============================================================
@buxoro_router.callback_query(MavjudData.filter(F.word=="mavjud"), BuxoroHomeSotishHovli.jihozlar)
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext, callback_data: MavjudData):
    text = "бор"
    # await callback_query.answer("Pressed")
    await state.update_data({
        "jihozlar": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=gazyoz, reply_markup=borYoq, parse_mode="HTML")
    await state.set_state(BuxoroHomeSotishHovli.gaz)


@buxoro_router.callback_query(JihozlarsizData.filter(F.word=="jihozlarsiz"), BuxoroHomeSotishHovli.jihozlar)
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext, callback_data: JihozlarsizData):
    text = "йўқ"
    # await callback_query.answer("Pressed")
    await state.update_data({
        "jihozlar": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=gazyoz, reply_markup=borYoq, parse_mode="HTML")
    await state.set_state(BuxoroHomeSotishHovli.gaz)


# ================================================================

@buxoro_router.callback_query(BorData.filter(F.word=="bor"), BuxoroHomeSotishHovli.gaz)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext, callback_data: BorData):
    text = "Газ ✔️"
    # await callback_query.answer("Танланди")

    await state.update_data({
        "gaz": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=svetyoz, reply_markup=borYoq, parse_mode="HTML")
    await state.set_state(BuxoroHomeSotishHovli.svet)


@buxoro_router.callback_query(YoqData.filter(F.word=="yoq"), BuxoroHomeSotishHovli.gaz)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext, callback_data: YoqData):
    text = "doesnotexist"
    # await callback_query.answer("Танланди")

    await state.update_data({
        "gaz": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=svetyoz, reply_markup=borYoq, parse_mode="HTML")
    await state.set_state(BuxoroHomeSotishHovli.svet)

# ========================================================================
    
@buxoro_router.callback_query(BorData.filter(F.word=="bor"), BuxoroHomeSotishHovli.svet)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext, callback_data: BorData):
    text = " Свет ✔️"
    # await callback_query.answer("Танланди")

    await state.update_data({
        "svet": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=suvyoz, reply_markup=borYoq, parse_mode="HTML")
    await state.set_state(BuxoroHomeSotishHovli.suv)


@buxoro_router.callback_query(YoqData.filter(F.word=="yoq"), BuxoroHomeSotishHovli.svet)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext, callback_data: YoqData):
    text = "doesnotexist"
    # await callback_query.answer("Танланди")

    await state.update_data({
        "svet": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=suvyoz, reply_markup=borYoq, parse_mode="HTML")
    await state.set_state(BuxoroHomeSotishHovli.suv)

# ============================================================================

@buxoro_router.callback_query(BorData.filter(F.word=="bor"), BuxoroHomeSotishHovli.suv)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext, callback_data: BorData):
    text = " Сув ✔️"
    # await callback_query.answer("Tanlandi")

    await state.update_data({
        "suv": text
    })

    await callback_query.message.answer(text=kanalizatsiyayoz, reply_markup=borYoq, parse_mode="HTML")

    await state.set_state(BuxoroHomeSotishHovli.kanal)


@buxoro_router.callback_query(YoqData.filter(F.word=="yoq"), BuxoroHomeSotishHovli.suv)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext, callback_data: YoqData):
    text = "doesnotexist"
    # await callback_query.answer("Tanlandi")

    await state.update_data({
        "suv": text
    })

    await callback_query.message.answer(text=kanalizatsiyayoz, reply_markup=borYoq, parse_mode="HTML")

    await state.set_state(BuxoroHomeSotishHovli.kanal)

# ============================================================================

@buxoro_router.callback_query(BorData.filter(F.word=="bor"), BuxoroHomeSotishHovli.kanal)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext, callback_data: BorData):
    text = " Канализация ✔️"
    # await callback_query.answer("Tanlandi")

    await state.update_data({
        "kanal": text
    })

    await callback_query.message.answer(text=qoshimchaMalumotyoz, reply_markup=otkazishButton, parse_mode="HTML")

    if callback_query.message.text == "⏭️ Кейингиси":
        await state.update_data({
            "qoshimchaMalumot": ""
        })
        await state.set_state(BuxoroHomeSotishHovli.qoshimchaMalumot)
    else:
        await state.set_state(BuxoroHomeSotishHovli.qoshimchaMalumot)


@buxoro_router.callback_query(YoqData.filter(F.word=="yoq"), BuxoroHomeSotishHovli.kanal)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext, callback_data: YoqData):
    text = "doesnotexist"
    # await callback_query.answer("Tanlandi")

    await state.update_data({
        "kanal": text
    })

    await callback_query.message.answer(text=qoshimchaMalumotyoz, reply_markup=otkazishButton, parse_mode="HTML")

    if callback_query.message.text == "⏭️ Кейингиси":
        await state.update_data({
            "qoshimchaMalumot": ""
        })
        await state.set_state(BuxoroHomeSotishHovli.qoshimchaMalumot)
    else:
        await state.set_state(BuxoroHomeSotishHovli.qoshimchaMalumot)

# ==============================================================

@buxoro_router.message(BuxoroHomeSotishHovli.qoshimchaMalumot)
async def umumiyMaydon(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "qoshimchaMalumot": text
    })
    await message.answer(text=valyutayoz, reply_markup=valyutaButton, parse_mode="HTML")

    await state.set_state(BuxoroHomeSotishHovli.valyuta)


# =================================================================

@buxoro_router.callback_query(USDData.filter(F.word=="usd"), BuxoroHomeSotishHovli.valyuta)
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext, callback_data: USDData):
    text = " $"
    # await callback_query.answer("Pressed")

    await state.update_data({
        "valyuta": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=narxiyoz,
                                reply_markup=types.ReplyKeyboardRemove(), parse_mode="HTML")

    await state.set_state(BuxoroHomeSotishHovli.narxi)


@buxoro_router.callback_query(SUMData.filter(F.word=="sum"), BuxoroHomeSotishHovli.valyuta)
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext, callback_data: SUMData):
    text = " сўм"
    # await callback_query.answer("Pressed")

    await state.update_data({
        "valyuta": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=narxiyoz,
                           reply_markup=types.ReplyKeyboardRemove(), parse_mode="HTML")

    await state.set_state(BuxoroHomeSotishHovli.narxi)


# ===============================================================

@buxoro_router.message(lambda message: message.text and not message.text.replace('.', '').replace(',', '').isdigit(),
                    BuxoroHomeSotishHovli.narxi)
async def check_narxi(message: types.Message):
    await message.reply(faqatRaqamyoz)


@buxoro_router.message(BuxoroHomeSotishHovli.narxi)
async def kvartira_narxi(message: types.Message, state: FSMContext):
    msg = int(message.text)

    number = "{:,}".format(msg).replace(",", ".")

    await state.update_data({
        "narxi": number
    })

    await message.answer(text=manzilyoz, parse_mode="HTML")

    await state.set_state(BuxoroHomeSotishHovli.manzil)


@buxoro_router.message(BuxoroHomeSotishHovli.manzil)
async def umumiyMaydon(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "manzil": text
    })
    await message.answer(text=moljalyoz, parse_mode="HTML")

    await state.set_state(BuxoroHomeSotishHovli.moljal)


@buxoro_router.message(BuxoroHomeSotishHovli.moljal)
async def umumiyMaydon(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "moljal": text
    })
    await message.answer(text=telraqam1yoz, parse_mode="HTML")

    await state.set_state(BuxoroHomeSotishHovli.telNumberOne)


@buxoro_router.message(BuxoroHomeSotishHovli.telNumberOne)
async def umumiyMaydon(message: types.Message, state: FSMContext):
    telNumber = message.text

    await state.update_data({
        "telNumberOne": telNumber
    })

    await message.answer(text=telraqam2yoz, reply_markup=otkazishButton, parse_mode="HTML")
    if message.text == "⏭️ Кейингиси":
        await state.update_data({
            "telNumberTwo": ""
        })
        await state.set_state(BuxoroHomeSotishHovli.telNumberTwo)
    else:
        await state.set_state(BuxoroHomeSotishHovli.telNumberTwo)


@buxoro_router.message(BuxoroHomeSotishHovli.telNumberTwo)
async def umumiyMaydon(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "telNumberTwo": text
    })

    chat_id = message.chat.id
    media_group = MediaGroupBuilder()

    data = await state.get_data()

    photos = data['images']

    
    if data['qoshimchaMalumot'] == "⏭️ Кейингиси" and data['telNumberTwo'] == "⏭️ Кейингиси":
        data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "-сотих" + "\n"
        data4 = "🔷 Хоналар сони: " + data['xonalar'] + "-та" + "\n"
        oshxona = "🔷 Ошхонаси: " + data['oshxona'] + "\n"
        hammom = "🔷 Ҳаммоми: " + data['hammom'] + "\n"
        data6 = "🔷 Неча қаватли: " + data['qavat'] + "-қаватли уй" + "\n"
        data7 = "🔷 Ремонти: " + data['remont'] + "\n"
        data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
        data9 = "🔷 "
        gaz = data['gaz']
        svet = data['svet']
        suv = data['suv']
        kanal = data['kanal']
        data10 = " бор\n\n"
        data12 = "💰 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
        data13 = "📌 Манзил: " + data['manzil'] + "\n"
        data14 = "📌 Мўлжал: " + data['moljal'] + "\n\n"
        data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"

        result = [buxororegion, data2, data3, data4, oshxona, hammom, data6, data7, data8, data9, gaz, svet, suv, kanal,
                  data10,
                  data12, data13, data14, data15]

        array = []

        for item in result:
            if item == "doesnotexist":
                continue

            array.append(item)

        stringify = "".join(array)
        cyrillic_text = to_cyrillic(stringify)

        media_group.add_photo(photos[0], caption=cyrillic_text)

        for file_id in photos[1:]:
            media_group.add_photo(f"{file_id}")

        await bot.send_media_group(chat_id=chat_id, media=media_group.build())
        await bot.send_message(chat_id=chat_id, text=check_text, reply_markup=checkbtn, parse_mode="HTML")
        await state.set_state(BuxoroHomeSotishHovli.check)
    elif data['qoshimchaMalumot'] == "⏭️ Кейингиси":
        data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "-сотих" + "\n"
        data4 = "🔷 Хоналар сони: " + data['xonalar'] + "-та" + "\n"
        oshxona = "🔷 Ошхонаси: " + data['oshxona'] + "\n"
        hammom = "🔷 Ҳаммоми: " + data['hammom'] + "\n"
        data6 = "🔷 Неча қаватли: " + data['qavat'] + "-қаватли уй" + "\n"
        data7 = "🔷 Ремонти: " + data['remont'] + "\n"
        data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
        data9 = "🔷 "
        gaz = data['gaz']
        svet = data['svet']
        suv = data['suv']
        kanal = data['kanal']
        data10 = " бор\n\n"
        data12 = "💰 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
        data13 = "📌 Манзил: " + data['manzil'] + "\n"
        data14 = "📌 Мўлжал: " + data['moljal'] + "\n\n"
        data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
        data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"

        result = [buxororegion, data2, data3, data4, oshxona, hammom, data6, data7, data8, data9, gaz, svet, suv, kanal,
                  data10,
                  data12, data13, data14, data15, data16]

        array = []

        for item in result:
            if item == "doesnotexist":
                continue

            array.append(item)

        stringify = "".join(array)
        cyrillic_text = to_cyrillic(stringify)

        media_group.add_photo(photos[0], caption=cyrillic_text)

        for file_id in photos[1:]:
            media_group.add_photo(f"{file_id}")

        await bot.send_media_group(chat_id=chat_id, media=media_group.build())
        await bot.send_message(chat_id=chat_id, text=check_text, reply_markup=checkbtn, parse_mode="HTML")
        await state.set_state(BuxoroHomeSotishHovli.check)

    elif data['telNumberTwo'] == "⏭️ Кейингиси":
        data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "-сотих" + "\n"
        data4 = "🔷 Хоналар сони: " + data['xonalar'] + "-та" + "\n"
        oshxona = "🔷 Ошхонаси: " + data['oshxona'] + "\n"
        hammom = "🔷 Ҳаммоми: " + data['hammom'] + "\n"
        data6 = "🔷 Неча қаватли: " + data['qavat'] + "-қаватли уй" + "\n"
        data7 = "🔷 Ремонти: " + data['remont'] + "\n"
        data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
        data9 = "🔷 "
        gaz = data['gaz']
        svet = data['svet']
        suv = data['suv']
        kanal = data['kanal']
        data10 = " бор\n"
        data11 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n\n"
        data12 = "💰 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
        data13 = "📌 Манзил: " + data['manzil'] + "\n"
        data14 = "📌 Мўлжал: " + data['moljal'] + "\n\n"
        data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"

        result = [buxororegion, data2, data3, data4, oshxona, hammom, data6, data7, data8, data9, gaz, svet, suv, kanal,
                  data10,
                  data11, data12, data13, data14, data15]

        array = []

        for item in result:
            if item == "doesnotexist":
                continue

            array.append(item)

        stringify = "".join(array)
        cyrillic_text = to_cyrillic(stringify)

        media_group.add_photo(photos[0], caption=cyrillic_text)

        for file_id in photos[1:]:
            media_group.add_photo(f"{file_id}")

        await bot.send_media_group(chat_id=chat_id, media=media_group.build())
        await bot.send_message(chat_id=chat_id, text=check_text, reply_markup=checkbtn, parse_mode="HTML")
        await state.set_state(BuxoroHomeSotishHovli.check)

    else:
        data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "-сотих" + "\n"
        data4 = "🔷 Хоналар сони: " + data['xonalar'] + "-та" + "\n"
        oshxona = "🔷 Ошхонаси: " + data['oshxona'] + "\n"
        hammom = "🔷 Ҳаммоми: " + data['hammom'] + "\n"
        data6 = "🔷 Неча қаватли: " + data['qavat'] + "-қаватли уй" + "\n"
        data7 = "🔷 Ремонти: " + data['remont'] + "\n"
        data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
        data9 = "🔷 "
        gaz = data['gaz']
        svet = data['svet']
        suv = data['suv']
        kanal = data['kanal']
        data10 = " бор\n"
        data11 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n\n"
        data12 = "💰 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
        data13 = "📌 Манзил: " + data['manzil'] + "\n"
        data14 = "📌 Мўлжал: " + data['moljal'] + "\n\n"
        data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
        data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"

        result = [buxororegion, data2, data3, data4, oshxona, hammom, data6, data7, data8, data9, gaz, svet, suv, kanal,
                  data10,
                  data11, data12, data13, data14, data15, data16]

        array = []

        for item in result:
            if item == "doesnotexist":
                continue

            array.append(item)

        stringify = "".join(array)
        cyrillic_text = to_cyrillic(stringify)

        media_group.add_photo(photos[0], caption=cyrillic_text)

        for file_id in photos[1:]:
            media_group.add_photo(f"{file_id}")

        await bot.send_media_group(chat_id=chat_id, media=media_group.build())
        await bot.send_message(chat_id=chat_id, text=check_text, reply_markup=checkbtn, parse_mode="HTML")
        await state.set_state(BuxoroHomeSotishHovli.check)


@buxoro_router.message(BuxoroHomeSotishHovli.check)
async def check(message: types.Message, state: FSMContext):
    mycheck = message.text
    chat_id = message.chat.id

    media_group = MediaGroupBuilder()

    if mycheck == "✅ Эълонни жойлаш":
        data = await state.get_data()
        photos = data['images']

        if data['qoshimchaMalumot'] == "⏭️ Кейингиси" and data['telNumberTwo'] == "⏭️ Кейингиси":
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "-сотих" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + "-та" + "\n"
            oshxona = "🔷 Ошхонаси: " + data['oshxona'] + "\n"
            hammom = "🔷 Ҳаммоми: " + data['hammom'] + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavat'] + "-қаватли уй" + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 "
            gaz = data['gaz']
            svet = data['svet']
            suv = data['suv']
            kanal = data['kanal']
            data10 = " бор\n\n"
            data12 = "💰 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data13 = "📌 Манзил: " + data['manzil'] + "\n"
            data14 = "📌 Мўлжал: " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"

            result = [buxororegion, data2, data3, data4, oshxona, hammom, data6, data7, data8, data9, gaz, svet, suv, kanal,
                      data10,
                      data12, data13, data14, data15]

            array = []

            for item in result:
                if item == "doesnotexist":
                    continue

                array.append(item)

            stringify = "".join(array)
            cyrillic_text = to_cyrillic(stringify)+data32+data33+data34+data35

            media_group.add_photo(photos[0], caption=cyrillic_text, parse_mode="HTML")

            for file_id in photos[1:]:
                media_group.add_photo(f"{file_id}")

            printer = await bot.send_media_group(chat_id=group_id, media=media_group.build())

            message_id = str(printer[-1].message_id)
            userId = str(message.chat.id)
            await db.add_yer_data(user_id=userId, photos=str(photos), captions=cyrillic_text, message_id=message_id)

            await bot.send_message(chat_id=group_id, text="Буйруқ Беринг", reply_markup=buxoro_group)
            await bot.send_message(chat_id=chat_id, text=success_text, reply_markup=start, parse_mode="HTML")
            await state.clear()

        elif data['qoshimchaMalumot'] == "⏭️ Кейингиси":
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "-сотих" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + "-та" + "\n"
            oshxona = "🔷 Ошхонаси: " + data['oshxona'] + "\n"
            hammom = "🔷 Ҳаммоми: " + data['hammom'] + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavat'] + "-қаватли уй" + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 "
            gaz = data['gaz']
            svet = data['svet']
            suv = data['suv']
            kanal = data['kanal']
            data10 = " бор\n\n"
            data12 = "💰 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data13 = "📌 Манзил: " + data['manzil'] + "\n"
            data14 = "📌 Мўлжал: " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
            data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"

            result = [buxororegion, data2, data3, data4, oshxona, hammom, data6, data7, data8, data9, gaz, svet, suv, kanal,
                      data10,
                      data12, data13, data14, data15, data16]

            array = []

            for item in result:
                if item == "doesnotexist":
                    continue

                array.append(item)

            stringify = "".join(array)
            cyrillic_text = to_cyrillic(stringify)+data32+data33+data34+data35

            media_group.add_photo(photos[0], caption=cyrillic_text, parse_mode="HTML")

            for file_id in photos[1:]:
                media_group.add_photo(f"{file_id}")

            printer = await bot.send_media_group(chat_id=group_id, media=media_group.build())

            message_id = str(printer[-1].message_id)
            userId = str(message.chat.id)
            await db.add_yer_data(user_id=userId, photos=str(photos), captions=cyrillic_text, message_id=message_id)

            await bot.send_message(chat_id=group_id, text="Буйруқ Беринг", reply_markup=buxoro_group)
            await bot.send_message(chat_id=chat_id, text=success_text, reply_markup=start, parse_mode="HTML")
            await state.clear()
        elif data["telNumberTwo"] == "⏭️ Кейингиси":
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "-сотих" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + "-та" + "\n"
            oshxona = "🔷 Ошхонаси: " + data['oshxona'] + "\n"
            hammom = "🔷 Ҳаммоми: " + data['hammom'] + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavat'] + "-қаватли уй" + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 "
            gaz = data['gaz']
            svet = data['svet']
            suv = data['suv']
            kanal = data['kanal']
            data10 = " бор\n"
            data11 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n\n"
            data12 = "💰 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data13 = "📌 Манзил: " + data['manzil'] + "\n"
            data14 = "📌 Мўлжал: " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"

            result = [buxororegion, data2, data3, data4, oshxona, hammom, data6, data7, data8, data9, gaz, svet, suv, kanal,
                      data10,
                      data11, data12, data13, data14, data15]

            array = []

            for item in result:
                if item == "doesnotexist":
                    continue

                array.append(item)

            stringify = "".join(array)
            cyrillic_text = to_cyrillic(stringify)+data32+data33+data34+data35

            media_group.add_photo(photos[0], caption=cyrillic_text, parse_mode="HTML")

            for file_id in photos[1:]:
                media_group.add_photo(f"{file_id}")

            printer = await bot.send_media_group(chat_id=group_id, media=media_group.build())

            message_id = str(printer[-1].message_id)
            userId = str(message.chat.id)
            await db.add_yer_data(user_id=userId, photos=str(photos), captions=cyrillic_text, message_id=message_id)

            await bot.send_message(chat_id=group_id, text="Буйруқ Беринг", reply_markup=buxoro_group)
            await bot.send_message(chat_id=chat_id, text=success_text, reply_markup=start, parse_mode="HTML")
            await state.clear()
        else:
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "-сотих" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + "-та" + "\n"
            oshxona = "🔷 Ошхонаси: " + data['oshxona'] + "\n"
            hammom = "🔷 Ҳаммоми: " + data['hammom'] + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavat'] + "-қаватли уй" + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 "
            gaz = data['gaz']
            svet = data['svet']
            suv = data['suv']
            kanal = data['kanal']
            data10 = " бор\n"
            data11 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n\n"
            data12 = "💰 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data13 = "📌 Манзил: " + data['manzil'] + "\n"
            data14 = "📌 Мўлжал: " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
            data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"

            result = [buxororegion, data2, data3, data4, oshxona, hammom, data6, data7, data8, data9, gaz, svet, suv, kanal,
                      data10,
                      data11, data12, data13, data14, data15, data16]

            array = []

            for item in result:
                if item == "doesnotexist":
                    continue

                array.append(item)

            stringify = "".join(array)
            cyrillic_text = to_cyrillic(stringify)+data32+data33+data34+data35

            media_group.add_photo(photos[0], caption=cyrillic_text, parse_mode="HTML")

            for file_id in photos[1:]:
                media_group.add_photo(f"{file_id}")

            printer = await bot.send_media_group(chat_id=group_id, media=media_group.build())

            message_id = str(printer[-1].message_id)
            userId = str(message.chat.id)
            await db.add_yer_data(user_id=userId, photos=str(photos), captions=cyrillic_text, message_id=message_id)

            await bot.send_message(chat_id=group_id, text="Буйруқ Беринг", reply_markup=buxoro_group)
            await bot.send_message(chat_id=chat_id, text=success_text, reply_markup=start, parse_mode="HTML")
            await state.clear()

    if mycheck == "❌ Эълонни қайтадан ёзиш":
        await bot.send_message(chat_id=chat_id, text="<b>❌ Эълон қабул қилинмади</b>", parse_mode="HTML")
        await bot.send_message(chat_id=chat_id, text="<b>Еълон бериш учун қайтадан уриниб кўринг</b>", reply_markup=start, parse_mode="HTML")
        await state.clear()


@buxoro_router.callback_query(IsGroupCall(), TasdiqlashBuxoro.filter(F.word == "buxorotasdiqlash"))
async def dokumentlar(call: types.CallbackQuery, state: FSMContext):
    chat_id = str(call.message.message_id - 1)

    media_group = MediaGroupBuilder()

    data = await db.yer_get_one_user_data(message_id=chat_id)

    photos_string = data['photos']

    try:
        photos_list = ast.literal_eval(photos_string)

    except (ValueError, SyntaxError) as e:
        await bot.send_message(chat_id=call.message.chat.id, text="Xatolik mavjud.")
        return

    media_group.add_photo(photos_list[0], caption=data['captions'], parse_mode="HTML")

    for file_id in photos_list[1:]:
        media_group.add_photo(file_id)

    await bot.send_media_group(chat_id=buxoro_id, media=media_group.build())
    await bot.send_message(chat_id=int(data['user_id']), text=success_message)
    await bot.send_message(chat_id=call.message.chat.id, text=success_message)
    


@buxoro_router.callback_query(IsGroupCall(), BekorQilishBuxoro.filter(F.word=="buxorobekor"))
async def dokumentlar(call: types.CallbackQuery, state: FSMContext):

    chat_id = str(call.message.message_id - 1)


    data = await db.yer_get_one_user_data(message_id=chat_id)

    await bot.send_message(chat_id=int(data['user_id']), text=fail_message)
    await bot.send_message(chat_id=call.message.chat.id, text=fail_message)