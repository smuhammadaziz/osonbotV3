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
from keyboards.inline.HomeButton import xorazm_group

from loader import bot, db
from states.KvartiraState.XorazmState import XorazmHomeSotish

from transliterate import to_cyrillic

from utils.QuestionKvartira.kvartiraqs import hovlitanlandi, rasmlar, umumiyMaydonyoz, faqatRaqamyoz, gazyoz, \
    jihozlaryoz, kanalizatsiyayoz, manzilyoz, moljalyoz, narxiyoz, nechaQavatyoz,oshxonayoz, \
    qoshimchaMalumotyoz, remontyoz, suvyoz, svetyoz, telraqam1yoz, telraqam2yoz, valyutayoz, \
    xammomyoz, xonalaryoz, xorazm_id, check_text, xorazmregion, data2, data32, data33, \
    data34, data35, success_text, nechanchiqavatyoz, group_id, success_message, fail_message


from keyboards.inline.data import XorazmKvartiraData

from keyboards.inline.data import YoqData, BorData
from keyboards.inline.data import YevroremontData, TamirlangantData, OrtachaData, TamirsizData
from keyboards.inline.data import MavjudData, JihozlarsizData
from keyboards.inline.data import USDData, SUMData
from keyboards.inline.data import TasdiqlashXorazm, BekorQilishXorazm


mode = "Markdown"

from aiogram_media_group import media_group_handler
from utils.media_group import MediaGroupBuilder


from filters.group_chat import IsGroup, IsGroupCall


xorazm_kv_router = Router()

@xorazm_kv_router.callback_query(XorazmKvartiraData.filter(F.word=="xorazmkv"))
async def first(callback_query: CallbackQuery, state: FSMContext, callback_data: XorazmKvartiraData):
    # await callback_query.answer(hovlitanlandi)
    await callback_query.message.answer(rasmlar, parse_mode="HTML")

    await state.set_state(XorazmHomeSotish.images)


@xorazm_kv_router.message(XorazmHomeSotish.images, F.media_group_id, F.content_type.in_({'photo'}))
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
    await state.set_state(XorazmHomeSotish.umumiyMaydon)



@xorazm_kv_router.message(lambda message: message.text and not message.text.replace('.', '').replace(',', '').isdigit(),
                    XorazmHomeSotish.umumiyMaydon)
async def check_umumiy(message: Message):
    await message.reply(faqatRaqamyoz)


@xorazm_kv_router.message(XorazmHomeSotish.umumiyMaydon)
async def umumiymaydon(message: Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "umumiyMaydon": text
    })

    await state.set_state(XorazmHomeSotish.xonalar)

    await bot.send_message(chat_id=message.chat.id, text=xonalaryoz, parse_mode="HTML")


@xorazm_kv_router.message(lambda message: message.text and not message.text.replace('.', '').replace(',', '').isdigit(),
                    XorazmHomeSotish.xonalar)
async def check_xonalar(message: Message):
    await message.reply(faqatRaqamyoz)


@xorazm_kv_router.message(XorazmHomeSotish.xonalar)
async def umumiymaydon(message: Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "xonalar": text
    })

    await bot.send_message(chat_id=message.chat.id, text=nechanchiqavatyoz, parse_mode="HTML")
    await state.set_state(XorazmHomeSotish.qavat)


@xorazm_kv_router.message(lambda message: message.text and not message.text.replace('.', '').replace(',', '').isdigit(),
                    XorazmHomeSotish.qavat)
async def check_qavat(message: types.Message):
    await message.reply(faqatRaqamyoz)


@xorazm_kv_router.message(XorazmHomeSotish.qavat)
async def umumiymaydon(message: types.Message, state: FSMContext):
    text = message.text

    await state.update_data({
        "qavat": text
    })

    await bot.send_message(chat_id=message.chat.id, text=nechaQavatyoz, parse_mode="HTML")
    await state.set_state(XorazmHomeSotish.qavatlik)


@xorazm_kv_router.message(lambda message: message.text and not message.text.replace('.', '').replace(',', '').isdigit(),
                    XorazmHomeSotish.qavatlik)
async def check_qavat(message: types.Message):
    await message.reply(faqatRaqamyoz)


@xorazm_kv_router.message(XorazmHomeSotish.qavatlik)
async def umumiymaydon(message: types.Message, state: FSMContext):
    text = message.text

    await state.update_data({
        "qavatlik": text
    })

    await bot.send_message(chat_id=message.chat.id, text=remontyoz, parse_mode="HTML", 
                           reply_markup=remontButton)
    await state.set_state(XorazmHomeSotish.remont)


# ====================================================================
@xorazm_kv_router.callback_query(YevroremontData.filter(F.word=="yevroremont"), XorazmHomeSotish.remont)
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext, callback_data: YevroremontData):
    text = "Евроремонт"
    # await callback_query.answer("Pressed")
    await state.update_data({
        "remont": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=jihozlaryoz,
                           reply_markup=jihozlarButton, parse_mode="HTML")
    await state.set_state(XorazmHomeSotish.jihozlar)


@xorazm_kv_router.callback_query(TamirlangantData.filter(F.word=="tamirlangan"), XorazmHomeSotish.remont)
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext, callback_data: TamirlangantData):
    text = "Таъмирланган"
    # await callback_query.answer("Pressed")
    await state.update_data({
        "remont": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=jihozlaryoz,
                           reply_markup=jihozlarButton, parse_mode="HTML")
    await state.set_state(XorazmHomeSotish.jihozlar)


@xorazm_kv_router.callback_query(OrtachaData.filter(F.word=="ortacha"), XorazmHomeSotish.remont)
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext, callback_data: OrtachaData):
    text = "Ўртача"
    # await callback_query.answer("Pressed")
    await state.update_data({
        "remont": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=jihozlaryoz,
                           reply_markup=jihozlarButton, parse_mode="HTML")
    await state.set_state(XorazmHomeSotish.jihozlar)


@xorazm_kv_router.callback_query(TamirsizData.filter(F.word=="tamirsiz"), XorazmHomeSotish.remont)
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext, callback_data: TamirsizData):
    text = "Таъмирсиз"
    # await callback_query.answer("Pressed")
    await state.update_data({
        "remont": text
    })


    await bot.send_message(chat_id=callback_query.message.chat.id, text=jihozlaryoz,
                           reply_markup=jihozlarButton, parse_mode="HTML")
    await state.set_state(XorazmHomeSotish.jihozlar)


# ===============================================================
@xorazm_kv_router.callback_query(MavjudData.filter(F.word=="mavjud"), XorazmHomeSotish.jihozlar)
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext, callback_data: MavjudData):
    text = "бор"
    # await callback_query.answer("Pressed")
    await state.update_data({
        "jihozlar": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=gazyoz, reply_markup=borYoq, parse_mode="HTML")
    await state.set_state(XorazmHomeSotish.gaz)


@xorazm_kv_router.callback_query(JihozlarsizData.filter(F.word=="jihozlarsiz"), XorazmHomeSotish.jihozlar)
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext, callback_data: JihozlarsizData):
    text = "йўқ"
    # await callback_query.answer("Pressed")
    await state.update_data({
        "jihozlar": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=gazyoz, reply_markup=borYoq, parse_mode="HTML")
    await state.set_state(XorazmHomeSotish.gaz)


# ================================================================

@xorazm_kv_router.callback_query(BorData.filter(F.word=="bor"), XorazmHomeSotish.gaz)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext, callback_data: BorData):
    text = "Газ ✔️"
    # await callback_query.answer("Танланди")

    await state.update_data({
        "gaz": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=svetyoz, reply_markup=borYoq, parse_mode="HTML")
    await state.set_state(XorazmHomeSotish.svet)


@xorazm_kv_router.callback_query(YoqData.filter(F.word=="yoq"), XorazmHomeSotish.gaz)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext, callback_data: YoqData):
    text = "doesnotexist"
    # await callback_query.answer("Танланди")

    await state.update_data({
        "gaz": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=svetyoz, reply_markup=borYoq, parse_mode="HTML")
    await state.set_state(XorazmHomeSotish.svet)

# ========================================================================
    
@xorazm_kv_router.callback_query(BorData.filter(F.word=="bor"), XorazmHomeSotish.svet)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext, callback_data: BorData):
    text = " Свет ✔️"
    # await callback_query.answer("Танланди")

    await state.update_data({
        "svet": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=suvyoz, reply_markup=borYoq, parse_mode="HTML")
    await state.set_state(XorazmHomeSotish.suv)


@xorazm_kv_router.callback_query(YoqData.filter(F.word=="yoq"), XorazmHomeSotish.svet)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext, callback_data: YoqData):
    text = "doesnotexist"
    # await callback_query.answer("Танланди")

    await state.update_data({
        "svet": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=suvyoz, reply_markup=borYoq, parse_mode="HTML")
    await state.set_state(XorazmHomeSotish.suv)

# ============================================================================

@xorazm_kv_router.callback_query(BorData.filter(F.word=="bor"), XorazmHomeSotish.suv)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext, callback_data: BorData):
    text = " Сув ✔️"
    # await callback_query.answer("Tanlandi")

    await state.update_data({
        "suv": text
    })

    await callback_query.message.answer(text=qoshimchaMalumotyoz, reply_markup=otkazishButton, parse_mode="HTML")

    if callback_query.message.text == "⏭️ Кейингиси":
        await state.update_data({
            "qoshimchaMalumot": ""
        })
        await state.set_state(XorazmHomeSotish.qoshimchaMalumot)
    else:
        await state.set_state(XorazmHomeSotish.qoshimchaMalumot)


@xorazm_kv_router.callback_query(YoqData.filter(F.word=="yoq"), XorazmHomeSotish.suv)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext, callback_data: YoqData):
    text = "doesnotexist"
    # await callback_query.answer("Tanlandi")

    await state.update_data({
        "suv": text
    })

    await callback_query.message.answer(text=qoshimchaMalumotyoz, reply_markup=otkazishButton, parse_mode="HTML")

    if callback_query.message.text == "⏭️ Кейингиси":
        await state.update_data({
            "qoshimchaMalumot": ""
        })
        await state.set_state(XorazmHomeSotish.qoshimchaMalumot)
    else:
        await state.set_state(XorazmHomeSotish.qoshimchaMalumot)

# ==============================================================

@xorazm_kv_router.message(XorazmHomeSotish.qoshimchaMalumot)
async def umumiyMaydon(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "qoshimchaMalumot": text
    })
    await message.answer(text=valyutayoz, reply_markup=valyutaButton, parse_mode="HTML")

    await state.set_state(XorazmHomeSotish.valyuta)


# =================================================================

@xorazm_kv_router.callback_query(USDData.filter(F.word=="usd"), XorazmHomeSotish.valyuta)
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext, callback_data: USDData):
    text = " $"
    # await callback_query.answer("Pressed")

    await state.update_data({
        "valyuta": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=narxiyoz,
                                reply_markup=types.ReplyKeyboardRemove(), parse_mode="HTML")

    await state.set_state(XorazmHomeSotish.narxi)


@xorazm_kv_router.callback_query(SUMData.filter(F.word=="sum"), XorazmHomeSotish.valyuta)
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext, callback_data: SUMData):
    text = " сўм"
    # await callback_query.answer("Pressed")

    await state.update_data({
        "valyuta": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=narxiyoz,
                                reply_markup=types.ReplyKeyboardRemove(), parse_mode="HTML")

    await state.set_state(XorazmHomeSotish.narxi)


# ===============================================================

@xorazm_kv_router.message(lambda message: message.text and not message.text.replace('.', '').replace(',', '').isdigit(),
                    XorazmHomeSotish.narxi)
async def check_narxi(message: types.Message):
    await message.reply(faqatRaqamyoz)


@xorazm_kv_router.message(XorazmHomeSotish.narxi)
async def kvartira_narxi(message: types.Message, state: FSMContext):
    msg = int(message.text)

    number = "{:,}".format(msg).replace(",", ".")

    await state.update_data({
        "narxi": number
    })

    await message.answer(text=manzilyoz, parse_mode="HTML")

    await state.set_state(XorazmHomeSotish.manzil)


@xorazm_kv_router.message(XorazmHomeSotish.manzil)
async def umumiyMaydon(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "manzil": text
    })
    await message.answer(text=moljalyoz, parse_mode="HTML")

    await state.set_state(XorazmHomeSotish.moljal)


@xorazm_kv_router.message(XorazmHomeSotish.moljal)
async def umumiyMaydon(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "moljal": text
    })
    await message.answer(text=telraqam1yoz, parse_mode="HTML")

    await state.set_state(XorazmHomeSotish.telNumberOne)


@xorazm_kv_router.message(XorazmHomeSotish.telNumberOne)
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
        await state.set_state(XorazmHomeSotish.telNumberTwo)
    else:
        await state.set_state(XorazmHomeSotish.telNumberTwo)


@xorazm_kv_router.message(XorazmHomeSotish.telNumberTwo)
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
        data3 = "🔶 Умумий майдон: " + data['umumiyMaydon'] + "-m²" + "\n"
        data4 = "🔶 Хоналар сони: " + data['xonalar'] + "-та" + "\n"
        data5 = "🔶 Қавати: " + data['qavat'] + "-қават" + "\n"
        data6 = "🔶 Неча қаватли: " + data['qavatlik'] + "-қаватли" + "\n"
        data7 = "🔶 Ремонти: " + data['remont'] + "\n"
        data8 = "🔶 Жиҳозлари: " + data['jihozlar'] + "\n"
        data9 = "🔶 "
        gaz = data['gaz']
        svet = data['svet']
        suv = data['suv']
        data10 = " бор\n\n"
        data12 = "💵 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
        data13 = "📌 Манзил: " + data['manzil'] + "\n"
        data14 = "📌 Мўлжал: " + data['moljal'] + "\n\n"
        data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"

        result = [xorazmregion, data2, data3, data4, data5, data6, data7, data8, data9, gaz, svet, suv, data10,
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
        await state.set_state(XorazmHomeSotish.check)
    elif data['qoshimchaMalumot'] == "⏭️ Кейингиси":
        data3 = "🔶 Умумий майдон: " + data['umumiyMaydon'] + "-m²" + "\n"
        data4 = "🔶 Хоналар сони: " + data['xonalar'] + "-та" + "\n"
        data5 = "🔶 Қавати: " + data['qavat'] + "-қават" + "\n"
        data6 = "🔶 Неча қаватли: " + data['qavatlik'] + "-қаватли" + "\n"
        data7 = "🔶 Ремонти: " + data['remont'] + "\n"
        data8 = "🔶 Жиҳозлари: " + data['jihozlar'] + "\n"
        data9 = "🔶 "
        gaz = data['gaz']
        svet = data['svet']
        suv = data['suv']
        data10 = " бор\n\n"
        data12 = "💵 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
        data13 = "📌 Манзил: " + data['manzil'] + "\n"
        data14 = "📌 Мўлжал: " + data['moljal'] + "\n\n"
        data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
        data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"

        result = [xorazmregion, data2, data3, data4, data5, data6, data7, data8, data9, gaz, svet, suv, data10,
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
        await state.set_state(XorazmHomeSotish.check)

    elif data['telNumberTwo'] == "⏭️ Кейингиси":
        data3 = "🔶 Умумий майдон: " + data['umumiyMaydon'] + "-m²" + "\n"
        data4 = "🔶 Хоналар сони: " + data['xonalar'] + "-та" + "\n"
        data5 = "🔶 Қавати: " + data['qavat'] + "-қават" + "\n"
        data6 = "🔶 Неча қаватли: " + data['qavatlik'] + "-қаватли" + "\n"
        data7 = "🔶 Ремонти: " + data['remont'] + "\n"
        data8 = "🔶 Жиҳозлари: " + data['jihozlar'] + "\n"
        data9 = "🔶 "
        gaz = data['gaz']
        svet = data['svet']
        suv = data['suv']
        data10 = " бор\n"
        data11 = "🔶 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n\n"
        data12 = "💵 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
        data13 = "📌 Манзил: " + data['manzil'] + "\n"
        data14 = "📌 Мўлжал: " + data['moljal'] + "\n\n"
        data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"

        result = [xorazmregion, data2, data3, data4, data5, data6, data7, data8, data9, gaz, svet, suv, data10,
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
        await state.set_state(XorazmHomeSotish.check)

    else:
        data3 = "🔶 Умумий майдон: " + data['umumiyMaydon'] + "-m²" + "\n"
        data4 = "🔶 Хоналар сони: " + data['xonalar'] + "-та" + "\n"
        data5 = "🔶 Қавати: " + data['qavat'] + "-қават" + "\n"
        data6 = "🔶 Неча қаватли: " + data['qavatlik'] + "-қаватли" + "\n"
        data7 = "🔶 Ремонти: " + data['remont'] + "\n"
        data8 = "🔶 Жиҳозлари: " + data['jihozlar'] + "\n"
        data9 = "🔶 "
        gaz = data['gaz']
        svet = data['svet']
        suv = data['suv']
        data10 = " бор\n"
        data11 = "🔶 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n\n"
        data12 = "💵 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
        data13 = "📌 Манзил: " + data['manzil'] + "\n"
        data14 = "📌 Мўлжал: " + data['moljal'] + "\n\n"
        data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
        data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"

        result = [xorazmregion, data2, data3, data4, data5, data6, data7, data8, data9, gaz, svet, suv, data10,
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
        await state.set_state(XorazmHomeSotish.check)


@xorazm_kv_router.message(XorazmHomeSotish.check)
async def check(message: types.Message, state: FSMContext):
    mycheck = message.text
    chat_id = message.chat.id

    media_group = MediaGroupBuilder()

    if mycheck == "✅ Эълонни жойлаш":
        data = await state.get_data()
        photos = data['images']

        if data['qoshimchaMalumot'] == "⏭️ Кейингиси" and data['telNumberTwo'] == "⏭️ Кейингиси":
            data3 = "🔶 Умумий майдон: " + data['umumiyMaydon'] + "-m²" + "\n"
            data4 = "🔶 Хоналар сони: " + data['xonalar'] + "-та" + "\n"
            data5 = "🔶 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔶 Неча қаватли: " + data['qavatlik'] + "-қаватли" + "\n"
            data7 = "🔶 Ремонти: " + data['remont'] + "\n"
            data8 = "🔶 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔶 "
            gaz = data['gaz']
            svet = data['svet']
            suv = data['suv']
            data10 = " бор\n\n"
            data12 = "💵 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data13 = "📌 Манзил: " + data['manzil'] + "\n"
            data14 = "📌 Мўлжал: " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"

            result = [xorazmregion, data2, data3, data4, data5, data6, data7, data8, data9, gaz, svet, suv, data10,
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

            await bot.send_message(chat_id=group_id, text="Буйруқ Беринг", reply_markup=xorazm_group)
            await bot.send_message(chat_id=chat_id, text=success_text, reply_markup=start, parse_mode="HTML")
            await state.clear()

        elif data['qoshimchaMalumot'] == "⏭️ Кейингиси":
            data3 = "🔶 Умумий майдон: " + data['umumiyMaydon'] + "-m²" + "\n"
            data4 = "🔶 Хоналар сони: " + data['xonalar'] + "-та" + "\n"
            data5 = "🔶 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔶 Неча қаватли: " + data['qavatlik'] + "-қаватли" + "\n"
            data7 = "🔶 Ремонти: " + data['remont'] + "\n"
            data8 = "🔶 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔶 "
            gaz = data['gaz']
            svet = data['svet']
            suv = data['suv']
            data10 = " бор\n\n"
            data12 = "💵 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data13 = "📌 Манзил: " + data['manzil'] + "\n"
            data14 = "📌 Мўлжал: " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
            data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"

            result = [xorazmregion, data2, data3, data4, data5, data6, data7, data8, data9, gaz, svet, suv, data10,
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

            await bot.send_message(chat_id=group_id, text="Буйруқ Беринг", reply_markup=xorazm_group)
            await bot.send_message(chat_id=chat_id, text=success_text, reply_markup=start, parse_mode="HTML")
            await state.clear()
        elif data["telNumberTwo"] == "⏭️ Кейингиси":
            data3 = "🔶 Умумий майдон: " + data['umumiyMaydon'] + "-m²" + "\n"
            data4 = "🔶 Хоналар сони: " + data['xonalar'] + "-та" + "\n"
            data5 = "🔶 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔶 Неча қаватли: " + data['qavatlik'] + "-қаватли" + "\n"
            data7 = "🔶 Ремонти: " + data['remont'] + "\n"
            data8 = "🔶 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔶 "
            gaz = data['gaz']
            svet = data['svet']
            suv = data['suv']
            data10 = " бор\n"
            data11 = "🔶 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n\n"
            data12 = "💵 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data13 = "📌 Манзил: " + data['manzil'] + "\n"
            data14 = "📌 Мўлжал: " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"

            result = [xorazmregion, data2, data3, data4, data5, data6, data7, data8, data9, gaz, svet, suv, data10,
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

            await bot.send_message(chat_id=group_id, text="Буйруқ Беринг", reply_markup=xorazm_group)
            await bot.send_message(chat_id=chat_id, text=success_text, reply_markup=start, parse_mode="HTML")
            await state.clear()
        else:
            data3 = "🔶 Умумий майдон: " + data['umumiyMaydon'] + "-m²" + "\n"
            data4 = "🔶 Хоналар сони: " + data['xonalar'] + "-та" + "\n"
            data5 = "🔶 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔶 Неча қаватли: " + data['qavatlik'] + "-қаватли" + "\n"
            data7 = "🔶 Ремонти: " + data['remont'] + "\n"
            data8 = "🔶 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔶 "
            gaz = data['gaz']
            svet = data['svet']
            suv = data['suv']
            data10 = " бор\n"
            data11 = "🔶 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n\n"
            data12 = "💵 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data13 = "📌 Манзил: " + data['manzil'] + "\n"
            data14 = "📌 Мўлжал: " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
            data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"

            result = [xorazmregion, data2, data3, data4, data5, data6, data7, data8, data9, gaz, svet, suv, data10,
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

            await bot.send_message(chat_id=group_id, text="Буйруқ Беринг", reply_markup=xorazm_group)
            await bot.send_message(chat_id=chat_id, text=success_text, reply_markup=start, parse_mode="HTML")
            await state.clear()

    if mycheck == "❌ Эълонни қайтадан ёзиш":
        await bot.send_message(chat_id=chat_id, text="<b>❌ Эълон қабул қилинмади</b>", parse_mode="HTML")
        await bot.send_message(chat_id=chat_id, text="<b>Еълон бериш учун қайтадан уриниб кўринг</b>", reply_markup=start, parse_mode="HTML")
        await state.clear()


@xorazm_kv_router.callback_query(IsGroupCall(), TasdiqlashXorazm.filter(F.word == "xorazmtasdiqlash"))
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

    await bot.send_media_group(chat_id=xorazm_id, media=media_group.build())
    await bot.send_message(chat_id=int(data['user_id']), text=success_message)
    await bot.send_message(chat_id=call.message.chat.id, text=success_message)
    


@xorazm_kv_router.callback_query(IsGroupCall(), BekorQilishXorazm.filter(F.word=="xorazmbekor"))
async def dokumentlar(call: types.CallbackQuery, state: FSMContext):

    chat_id = str(call.message.message_id - 1)


    data = await db.yer_get_one_user_data(message_id=chat_id)

    await bot.send_message(chat_id=int(data['user_id']), text=fail_message)
    await bot.send_message(chat_id=call.message.chat.id, text=fail_message)