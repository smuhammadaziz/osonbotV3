from typing import List

from aiogram import types, F, Router

from aiogram.types import Message

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types.callback_query import CallbackQuery

from keyboards.default.JobButton import checkbtn, start
from keyboards.default.JobButton import otkazishButton
from keyboards.inline.HomeButton import remontButton, jihozlarButton, valyutaButton, borYoq
from loader import bot
from states.KvartiraState.ToshVilState import ToshkentVilHomeSotish

from transliterate import to_cyrillic

from utils.QuestionKvartira.kvartiraqs import hovlitanlandi, rasmlar, umumiyMaydonyoz, faqatRaqamyoz, gazyoz, \
    jihozlaryoz, kanalizatsiyayoz, manzilyoz, moljalyoz, narxiyoz, nechaQavatyoz,oshxonayoz, \
    qoshimchaMalumotyoz, remontyoz, suvyoz, svetyoz, telraqam1yoz, telraqam2yoz, valyutayoz, \
    xammomyoz, xonalaryoz, toshvil_id, check_text, toshkentvilregion, data2, data32, data33, \
    data34, data35, success_text, nechanchiqavatyoz


from keyboards.inline.data import ToshkentVilKvartiraData

from keyboards.inline.data import YoqData, BorData
from keyboards.inline.data import YevroremontData, TamirlangantData, OrtachaData, TamirsizData
from keyboards.inline.data import MavjudData, JihozlarsizData
from keyboards.inline.data import USDData, SUMData


mode = "Markdown"

from aiogram_media_group import media_group_handler

from aiogram.utils.media_group import MediaGroupBuilder



toshvil_kv_router = Router()

@toshvil_kv_router.callback_query(ToshkentVilKvartiraData.filter(F.word=="toshvilkv"))
async def first(callback_query: CallbackQuery, state: FSMContext, callback_data: ToshkentVilKvartiraData):
    # await callback_query.answer(hovlitanlandi)
    await callback_query.message.answer(rasmlar, parse_mode="HTML")

    await state.set_state(ToshkentVilHomeSotish.images)


@toshvil_kv_router.message(ToshkentVilHomeSotish.images, F.media_group_id, F.content_type.in_({'photo'}))
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
    await state.set_state(ToshkentVilHomeSotish.umumiyMaydon)



@toshvil_kv_router.message(lambda message: message.text and not message.text.replace('.', '').replace(',', '').isdigit(),
                    ToshkentVilHomeSotish.umumiyMaydon)
async def check_umumiy(message: Message):
    await message.reply(faqatRaqamyoz)


@toshvil_kv_router.message(ToshkentVilHomeSotish.umumiyMaydon)
async def umumiymaydon(message: Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "umumiyMaydon": text
    })

    await state.set_state(ToshkentVilHomeSotish.xonalar)

    await bot.send_message(chat_id=message.chat.id, text=xonalaryoz, parse_mode="HTML")


@toshvil_kv_router.message(lambda message: message.text and not message.text.replace('.', '').replace(',', '').isdigit(),
                    ToshkentVilHomeSotish.xonalar)
async def check_xonalar(message: Message):
    await message.reply(faqatRaqamyoz)


@toshvil_kv_router.message(ToshkentVilHomeSotish.xonalar)
async def umumiymaydon(message: Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "xonalar": text
    })

    await bot.send_message(chat_id=message.chat.id, text=nechanchiqavatyoz, parse_mode="HTML")
    await state.set_state(ToshkentVilHomeSotish.qavat)


@toshvil_kv_router.message(lambda message: message.text and not message.text.replace('.', '').replace(',', '').isdigit(),
                    ToshkentVilHomeSotish.qavat)
async def check_qavat(message: types.Message):
    await message.reply(faqatRaqamyoz)


@toshvil_kv_router.message(ToshkentVilHomeSotish.qavat)
async def umumiymaydon(message: types.Message, state: FSMContext):
    text = message.text

    await state.update_data({
        "qavat": text
    })

    await bot.send_message(chat_id=message.chat.id, text=nechaQavatyoz, parse_mode="HTML")
    await state.set_state(ToshkentVilHomeSotish.qavatlik)


@toshvil_kv_router.message(lambda message: message.text and not message.text.replace('.', '').replace(',', '').isdigit(),
                    ToshkentVilHomeSotish.qavatlik)
async def check_qavat(message: types.Message):
    await message.reply(faqatRaqamyoz)


@toshvil_kv_router.message(ToshkentVilHomeSotish.qavatlik)
async def umumiymaydon(message: types.Message, state: FSMContext):
    text = message.text

    await state.update_data({
        "qavatlik": text
    })

    await bot.send_message(chat_id=message.chat.id, text=remontyoz, parse_mode="HTML", 
                           reply_markup=remontButton)
    await state.set_state(ToshkentVilHomeSotish.remont)


# ====================================================================
@toshvil_kv_router.callback_query(YevroremontData.filter(F.word=="yevroremont"), ToshkentVilHomeSotish.remont)
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext, callback_data: YevroremontData):
    text = "Евроремонт"
    # await callback_query.answer("Pressed")
    await state.update_data({
        "remont": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=jihozlaryoz,
                           reply_markup=jihozlarButton, parse_mode="HTML")
    await state.set_state(ToshkentVilHomeSotish.jihozlar)


@toshvil_kv_router.callback_query(TamirlangantData.filter(F.word=="tamirlangan"), ToshkentVilHomeSotish.remont)
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext, callback_data: TamirlangantData):
    text = "Таъмирланган"
    # await callback_query.answer("Pressed")
    await state.update_data({
        "remont": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=jihozlaryoz,
                           reply_markup=jihozlarButton, parse_mode="HTML")
    await state.set_state(ToshkentVilHomeSotish.jihozlar)


@toshvil_kv_router.callback_query(OrtachaData.filter(F.word=="ortacha"), ToshkentVilHomeSotish.remont)
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext, callback_data: OrtachaData):
    text = "Ўртача"
    # await callback_query.answer("Pressed")
    await state.update_data({
        "remont": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=jihozlaryoz,
                           reply_markup=jihozlarButton, parse_mode="HTML")
    await state.set_state(ToshkentVilHomeSotish.jihozlar)


@toshvil_kv_router.callback_query(TamirsizData.filter(F.word=="tamirsiz"), ToshkentVilHomeSotish.remont)
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext, callback_data: TamirsizData):
    text = "Таъмирсиз"
    # await callback_query.answer("Pressed")
    await state.update_data({
        "remont": text
    })


    await bot.send_message(chat_id=callback_query.message.chat.id, text=jihozlaryoz,
                           reply_markup=jihozlarButton, parse_mode="HTML")
    await state.set_state(ToshkentVilHomeSotish.jihozlar)


# ===============================================================
@toshvil_kv_router.callback_query(MavjudData.filter(F.word=="mavjud"), ToshkentVilHomeSotish.jihozlar)
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext, callback_data: MavjudData):
    text = "бор"
    # await callback_query.answer("Pressed")
    await state.update_data({
        "jihozlar": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=gazyoz, reply_markup=borYoq, parse_mode="HTML")
    await state.set_state(ToshkentVilHomeSotish.gaz)


@toshvil_kv_router.callback_query(JihozlarsizData.filter(F.word=="jihozlarsiz"), ToshkentVilHomeSotish.jihozlar)
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext, callback_data: JihozlarsizData):
    text = "йўқ"
    # await callback_query.answer("Pressed")
    await state.update_data({
        "jihozlar": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=gazyoz, reply_markup=borYoq, parse_mode="HTML")
    await state.set_state(ToshkentVilHomeSotish.gaz)


# ================================================================

@toshvil_kv_router.callback_query(BorData.filter(F.word=="bor"), ToshkentVilHomeSotish.gaz)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext, callback_data: BorData):
    text = "Газ ✔️"
    # await callback_query.answer("Танланди")

    await state.update_data({
        "gaz": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=svetyoz, reply_markup=borYoq, parse_mode="HTML")
    await state.set_state(ToshkentVilHomeSotish.svet)


@toshvil_kv_router.callback_query(YoqData.filter(F.word=="yoq"), ToshkentVilHomeSotish.gaz)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext, callback_data: YoqData):
    text = "doesnotexist"
    # await callback_query.answer("Танланди")

    await state.update_data({
        "gaz": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=svetyoz, reply_markup=borYoq, parse_mode="HTML")
    await state.set_state(ToshkentVilHomeSotish.svet)

# ========================================================================
    
@toshvil_kv_router.callback_query(BorData.filter(F.word=="bor"), ToshkentVilHomeSotish.svet)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext, callback_data: BorData):
    text = " Свет ✔️"
    # await callback_query.answer("Танланди")

    await state.update_data({
        "svet": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=suvyoz, reply_markup=borYoq, parse_mode="HTML")
    await state.set_state(ToshkentVilHomeSotish.suv)


@toshvil_kv_router.callback_query(YoqData.filter(F.word=="yoq"), ToshkentVilHomeSotish.svet)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext, callback_data: YoqData):
    text = "doesnotexist"
    # await callback_query.answer("Танланди")

    await state.update_data({
        "svet": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=suvyoz, reply_markup=borYoq, parse_mode="HTML")
    await state.set_state(ToshkentVilHomeSotish.suv)

# ============================================================================

@toshvil_kv_router.callback_query(BorData.filter(F.word=="bor"), ToshkentVilHomeSotish.suv)
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
        await state.set_state(ToshkentVilHomeSotish.qoshimchaMalumot)
    else:
        await state.set_state(ToshkentVilHomeSotish.qoshimchaMalumot)


@toshvil_kv_router.callback_query(YoqData.filter(F.word=="yoq"), ToshkentVilHomeSotish.suv)
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
        await state.set_state(ToshkentVilHomeSotish.qoshimchaMalumot)
    else:
        await state.set_state(ToshkentVilHomeSotish.qoshimchaMalumot)

# ==============================================================

@toshvil_kv_router.message(ToshkentVilHomeSotish.qoshimchaMalumot)
async def umumiyMaydon(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "qoshimchaMalumot": text
    })
    await message.answer(text=valyutayoz, reply_markup=valyutaButton, parse_mode="HTML")

    await state.set_state(ToshkentVilHomeSotish.valyuta)


# =================================================================

@toshvil_kv_router.callback_query(USDData.filter(F.word=="usd"), ToshkentVilHomeSotish.valyuta)
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext, callback_data: USDData):
    text = " $"
    # await callback_query.answer("Pressed")

    await state.update_data({
        "valyuta": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=narxiyoz,
                                reply_markup=types.ReplyKeyboardRemove(), parse_mode="HTML")

    await state.set_state(ToshkentVilHomeSotish.narxi)


@toshvil_kv_router.callback_query(SUMData.filter(F.word=="sum"), ToshkentVilHomeSotish.valyuta)
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext, callback_data: SUMData):
    text = " сўм"
    # await callback_query.answer("Pressed")

    await state.update_data({
        "valyuta": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=narxiyoz,
                                reply_markup=types.ReplyKeyboardRemove(), parse_mode="HTML")

    await state.set_state(ToshkentVilHomeSotish.narxi)


# ===============================================================

@toshvil_kv_router.message(lambda message: message.text and not message.text.replace('.', '').replace(',', '').isdigit(),
                    ToshkentVilHomeSotish.narxi)
async def check_narxi(message: types.Message):
    await message.reply(faqatRaqamyoz)


@toshvil_kv_router.message(ToshkentVilHomeSotish.narxi)
async def kvartira_narxi(message: types.Message, state: FSMContext):
    msg = int(message.text)

    number = "{:,}".format(msg).replace(",", ".")

    await state.update_data({
        "narxi": number
    })

    await message.answer(text=manzilyoz, parse_mode="HTML")

    await state.set_state(ToshkentVilHomeSotish.manzil)


@toshvil_kv_router.message(ToshkentVilHomeSotish.manzil)
async def umumiyMaydon(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "manzil": text
    })
    await message.answer(text=moljalyoz, parse_mode="HTML")

    await state.set_state(ToshkentVilHomeSotish.moljal)


@toshvil_kv_router.message(ToshkentVilHomeSotish.moljal)
async def umumiyMaydon(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "moljal": text
    })
    await message.answer(text=telraqam1yoz, parse_mode="HTML")

    await state.set_state(ToshkentVilHomeSotish.telNumberOne)


@toshvil_kv_router.message(ToshkentVilHomeSotish.telNumberOne)
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
        await state.set_state(ToshkentVilHomeSotish.telNumberTwo)
    else:
        await state.set_state(ToshkentVilHomeSotish.telNumberTwo)


@toshvil_kv_router.message(ToshkentVilHomeSotish.telNumberTwo)
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

        result = [toshkentvilregion, data2, data3, data4, data5, data6, data7, data8, data9, gaz, svet, suv, data10,
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
        await state.set_state(ToshkentVilHomeSotish.check)
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

        result = [toshkentvilregion, data2, data3, data4, data5, data6, data7, data8, data9, gaz, svet, suv, data10,
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
        await state.set_state(ToshkentVilHomeSotish.check)

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

        result = [toshkentvilregion, data2, data3, data4, data5, data6, data7, data8, data9, gaz, svet, suv, data10,
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
        await state.set_state(ToshkentVilHomeSotish.check)

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

        result = [toshkentvilregion, data2, data3, data4, data5, data6, data7, data8, data9, gaz, svet, suv, data10,
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
        await state.set_state(ToshkentVilHomeSotish.check)


@toshvil_kv_router.message(ToshkentVilHomeSotish.check)
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

            result = [toshkentvilregion, data2, data3, data4, data5, data6, data7, data8, data9, gaz, svet, suv, data10,
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

            await bot.send_media_group(chat_id=toshvil_id, media=media_group.build())
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

            result = [toshkentvilregion, data2, data3, data4, data5, data6, data7, data8, data9, gaz, svet, suv, data10,
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

            await bot.send_media_group(chat_id=toshvil_id, media=media_group.build())
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

            result = [toshkentvilregion, data2, data3, data4, data5, data6, data7, data8, data9, gaz, svet, suv, data10,
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

            await bot.send_media_group(chat_id=toshvil_id, media=media_group.build())
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

            result = [toshkentvilregion, data2, data3, data4, data5, data6, data7, data8, data9, gaz, svet, suv, data10,
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

            await bot.send_media_group(chat_id=toshvil_id, media=media_group.build())
            await bot.send_message(chat_id=chat_id, text=success_text, reply_markup=start, parse_mode="HTML")
            await state.clear()

    if mycheck == "❌ Эълонни қайтадан ёзиш":
        await bot.send_message(chat_id=chat_id, text="<b>❌ Эълон қабул қилинмади</b>", parse_mode="HTML")
        await bot.send_message(chat_id=chat_id, text="<b>Еълон бериш учун қайтадан уриниб кўринг</b>", reply_markup=start, parse_mode="HTML")
        await state.clear()