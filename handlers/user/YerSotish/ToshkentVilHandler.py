import ast
from typing import List
from aiogram import Bot, types, F, Router
from aiogram.types import Message

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types.callback_query import CallbackQuery

from keyboards.default.JobButton import checkbtn, start
from keyboards.default.JobButton import otkazishButton
from keyboards.inline.HomeButton import remontButton, documentButton, valyutaButton, borYoq
from keyboards.inline.HomeButton import toshvil_group

from loader import bot, db
from states.YerSotish.ToshkentVilState import ToshkentVilYerSotish

from transliterate import to_cyrillic

from utils.QuestionYer.yerqs import hovlitanlandi, rasmlar, umumiyMaydonyoz, faqatRaqamyoz, gazyoz, \
    jihozlaryoz, kanalizatsiyayoz, manzilyoz, moljalyoz, narxiyoz, nechaQavatyoz,oshxonayoz, \
    qoshimchaMalumotyoz, remontyoz, suvyoz, svetyoz, telraqam1yoz, telraqam2yoz, valyutayoz, \
    xammomyoz, xonalaryoz, toshvil_id, check_text, toshkentvilregion, data2, data32, data33, \
    data34, data35, success_text, hujjatlaribormiyoz, group_id, success_message, fail_message


from keyboards.inline.data import ToshkentVilYerData

from keyboards.inline.data import YoqData, BorData
from keyboards.inline.data import DocumentHaveData, DocumentNotData
from keyboards.inline.data import USDData, SUMData
from keyboards.inline.data import TasdiqlashToshvil, BekorQilishToshvil

mode = "Markdown"

from aiogram_media_group import media_group_handler
from utils.media_group import MediaGroupBuilder


from filters.group_chat import IsGroup, IsGroupCall


toshvil_yer_router = Router()

@toshvil_yer_router.callback_query(ToshkentVilYerData.filter(F.word=="toshvilyer"))
async def first(callback_query: CallbackQuery, state: FSMContext, callback_data: ToshkentVilYerData):
    # await callback_query.answer(hovlitanlandi)
    await callback_query.message.answer(rasmlar, parse_mode="HTML")

    await state.set_state(ToshkentVilYerSotish.images)


@toshvil_yer_router.message(ToshkentVilYerSotish.images, F.media_group_id, F.content_type.in_({'photo'}))
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
    await state.set_state(ToshkentVilYerSotish.umumiyMaydon)


@toshvil_yer_router.message(lambda message: message.text and not message.text.replace('.', '').replace(',', '').isdigit(),
                    ToshkentVilYerSotish.umumiyMaydon)
async def check_umumiy(message: Message):
    await message.reply(faqatRaqamyoz)


@toshvil_yer_router.message(ToshkentVilYerSotish.umumiyMaydon)
async def umumiymaydon(message: Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "umumiyMaydon": text
    })

    await bot.send_message(chat_id=message.chat.id, text=gazyoz, reply_markup=borYoq, parse_mode="HTML")

    await state.set_state(ToshkentVilYerSotish.gaz)


# ================================================================

@toshvil_yer_router.callback_query(BorData.filter(F.word=="bor"), ToshkentVilYerSotish.gaz)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext, callback_data: BorData):
    text = "Газ ✔️"
    # await callback_query.answer("Танланди")

    await state.update_data({
        "gaz": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=svetyoz, reply_markup=borYoq)
    await state.set_state(ToshkentVilYerSotish.svet)


@toshvil_yer_router.callback_query(YoqData.filter(F.word=="yoq"), ToshkentVilYerSotish.gaz)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext, callback_data: YoqData):
    text = "doesnotexist"
    # await callback_query.answer("Танланди")

    await state.update_data({
        "gaz": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=svetyoz, reply_markup=borYoq)
    await state.set_state(ToshkentVilYerSotish.svet)

# ========================================================================
    
@toshvil_yer_router.callback_query(BorData.filter(F.word=="bor"), ToshkentVilYerSotish.svet)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext, callback_data: BorData):
    text = " Свет ✔️"
    # await callback_query.answer("Танланди")

    await state.update_data({
        "svet": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=suvyoz, reply_markup=borYoq)
    await state.set_state(ToshkentVilYerSotish.suv)


@toshvil_yer_router.callback_query(YoqData.filter(F.word=="yoq"), ToshkentVilYerSotish.svet)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext, callback_data: YoqData):
    text = "doesnotexist"
    # await callback_query.answer("Танланди")

    await state.update_data({
        "svet": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=suvyoz, reply_markup=borYoq)
    await state.set_state(ToshkentVilYerSotish.suv)

# ============================================================================

@toshvil_yer_router.callback_query(BorData.filter(F.word=="bor"), ToshkentVilYerSotish.suv)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext, callback_data: BorData):
    text = " Сув ✔️"
    # await callback_query.answer("Tanlandi")

    await state.update_data({
        "suv": text
    })

    await callback_query.message.answer(text=kanalizatsiyayoz, reply_markup=borYoq, parse_mode="HTML")

    await state.set_state(ToshkentVilYerSotish.kanal)


@toshvil_yer_router.callback_query(YoqData.filter(F.word=="yoq"), ToshkentVilYerSotish.suv)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext, callback_data: YoqData):
    text = "doesnotexist"
    # await callback_query.answer("Tanlandi")

    await state.update_data({
        "suv": text
    })

    await callback_query.message.answer(text=kanalizatsiyayoz, reply_markup=borYoq, parse_mode="HTML")

    await state.set_state(ToshkentVilYerSotish.kanal)

# ============================================================================

@toshvil_yer_router.callback_query(BorData.filter(F.word=="bor"), ToshkentVilYerSotish.kanal)
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
        await state.set_state(ToshkentVilYerSotish.qoshimchaMalumot)
    else:
        await state.set_state(ToshkentVilYerSotish.qoshimchaMalumot)


@toshvil_yer_router.callback_query(YoqData.filter(F.word=="yoq"), ToshkentVilYerSotish.kanal)
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
        await state.set_state(ToshkentVilYerSotish.qoshimchaMalumot)
    else:
        await state.set_state(ToshkentVilYerSotish.qoshimchaMalumot)

# ==============================================================

@toshvil_yer_router.message(ToshkentVilYerSotish.qoshimchaMalumot)
async def umumiyMaydon(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "qoshimchaMalumot": text
    })
    await message.answer(text=hujjatlaribormiyoz, reply_markup=documentButton, parse_mode="HTML")

    await state.set_state(ToshkentVilYerSotish.hujjatlar)


# =================================================================
    
@toshvil_yer_router.callback_query(DocumentHaveData.filter(F.word=="dokumentbor"), ToshkentVilYerSotish.hujjatlar)
async def dokumentlar(callback_query: types.CallbackQuery, state: FSMContext):
    text = "Бор,  қонуний"
    # await callback_query.answer("Dokument bor")

    await state.update_data({
        "hujjatlar": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=valyutayoz,
                           reply_markup=valyutaButton, parse_mode="HTML")

    await state.set_state(ToshkentVilYerSotish.valyuta)


@toshvil_yer_router.callback_query(DocumentNotData.filter(F.word=="dokumentyoq"), ToshkentVilYerSotish.hujjatlar)
async def dokumentlar(callback_query: types.CallbackQuery, state: FSMContext):
    text = "Тайёр эмас"
    # await callback_query.answer("Dokument Yo'q")

    await state.update_data({
        "hujjatlar": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=valyutayoz,
                           reply_markup=valyutaButton, parse_mode="HTML")

    await state.set_state(ToshkentVilYerSotish.valyuta)    

# =================================================================
    

@toshvil_yer_router.callback_query(USDData.filter(F.word=="usd"), ToshkentVilYerSotish.valyuta)
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext, callback_data: USDData):
    text = " $"
    # await callback_query.answer("Pressed")

    await state.update_data({
        "valyuta": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=narxiyoz,
                                reply_markup=types.ReplyKeyboardRemove(), parse_mode="HTML")

    await state.set_state(ToshkentVilYerSotish.narxi)


@toshvil_yer_router.callback_query(SUMData.filter(F.word=="sum"), ToshkentVilYerSotish.valyuta)
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext, callback_data: SUMData):
    text = " сўм"
    # await callback_query.answer("Pressed")

    await state.update_data({
        "valyuta": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=narxiyoz,
                                reply_markup=types.ReplyKeyboardRemove(), parse_mode="HTML")

    await state.set_state(ToshkentVilYerSotish.narxi)


# ===============================================================

@toshvil_yer_router.message(lambda message: message.text and not message.text.replace('.', '').replace(',', '').isdigit(),
                    ToshkentVilYerSotish.narxi)
async def check_narxi(message: types.Message):
    await message.reply(faqatRaqamyoz)


@toshvil_yer_router.message(ToshkentVilYerSotish.narxi)
async def kvartira_narxi(message: types.Message, state: FSMContext):
    msg = int(message.text)

    number = "{:,}".format(msg).replace(",", ".")

    await state.update_data({
        "narxi": number
    })

    await message.answer(text=manzilyoz, parse_mode="HTML")

    await state.set_state(ToshkentVilYerSotish.manzil)


@toshvil_yer_router.message(ToshkentVilYerSotish.manzil)
async def umumiyMaydon(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "manzil": text
    })
    await message.answer(text=moljalyoz, parse_mode="HTML")

    await state.set_state(ToshkentVilYerSotish.moljal)


@toshvil_yer_router.message(ToshkentVilYerSotish.moljal)
async def umumiyMaydon(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "moljal": text
    })
    await message.answer(text=telraqam1yoz, parse_mode="HTML")

    await state.set_state(ToshkentVilYerSotish.telNumberOne)


@toshvil_yer_router.message(ToshkentVilYerSotish.telNumberOne)
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
        await state.set_state(ToshkentVilYerSotish.telNumberTwo)
    else:
        await state.set_state(ToshkentVilYerSotish.telNumberTwo)


@toshvil_yer_router.message(ToshkentVilYerSotish.telNumberTwo)
async def telNumbertwo(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "telNumberTwo": text
    })

    chat_id = message.chat.id
    media_group = MediaGroupBuilder()

    data = await state.get_data()

    photos = data['images']

    if data['qoshimchaMalumot'] == "⏭️ Кейингиси" and data['telNumberTwo'] == "⏭️ Кейингиси":
        data3 = "♦️ Умумий майдон: " + data['umumiyMaydon'] + "-сотих" + "\n"
        data9 = "♦️ "
        gaz = data['gaz']
        svet = data['svet']
        suv = data['suv']
        kanal = data['kanal']
        data10 = " бор\n"
        document = "♦️ Ҳужжатлари: " + data['hujjatlar'] + "\n\n"
        data12 = "💲 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
        data13 = "📌 Манзил: " + data['manzil'] + "\n"
        data14 = "📌 Мўлжал: " + data['moljal'] + "\n\n"
        data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"

        result = [toshkentvilregion, data2, data3, data9, gaz, svet, suv, kanal, data10, document,
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
        await state.set_state(ToshkentVilYerSotish.check)
    elif data['qoshimchaMalumot'] == "⏭️ Кейингиси":
        data3 = "♦️ Умумий майдон: " + data['umumiyMaydon'] + "-сотих" + "\n"
        data9 = "♦️ "
        gaz = data['gaz']
        svet = data['svet']
        suv = data['suv']
        kanal = data['kanal']
        data10 = " бор\n"
        document = "♦️ Ҳужжатлари: " + data['hujjatlar'] + "\n\n"
        data12 = "💲 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
        data13 = "📌 Манзил: " + data['manzil'] + "\n"
        data14 = "📌 Мўлжал: " + data['moljal'] + "\n\n"
        data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
        data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"

        result = [toshkentvilregion, data2, data3, data9, gaz, svet, suv, kanal, data10, document,
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
        await state.set_state(ToshkentVilYerSotish.check)

    elif data['telNumberTwo'] == "⏭️ Кейингиси":
        data3 = "♦️ Умумий майдон: " + data['umumiyMaydon'] + "-сотих" + "\n"
        data9 = "♦️ "
        gaz = data['gaz']
        svet = data['svet']
        suv = data['suv']
        kanal = data['kanal']
        data10 = " бор\n"
        document = "♦️ Ҳужжатлари: " + data['hujjatlar'] + "\n"
        data11 = "♦️ Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n\n"
        data12 = "💲 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
        data13 = "📌 Манзил: " + data['manzil'] + "\n"
        data14 = "📌 Мўлжал: " + data['moljal'] + "\n\n"
        data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"

        result = [toshkentvilregion, data2, data3, data9, gaz, svet, suv, kanal, data10, document,
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
        await state.set_state(ToshkentVilYerSotish.check)

    else:
        data3 = "♦️ Умумий майдон: " + data['umumiyMaydon'] + "-сотих" + "\n"
        data9 = "♦️ "
        gaz = data['gaz']
        svet = data['svet']
        suv = data['suv']
        kanal = data['kanal']
        data10 = " бор\n"
        document = "♦️ Ҳужжатлари: " + data['hujjatlar'] + "\n"
        data11 = "♦️ Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n\n"
        data12 = "💲 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
        data13 = "📌 Манзил: " + data['manzil'] + "\n"
        data14 = "📌 Мўлжал: " + data['moljal'] + "\n\n"
        data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
        data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"

        result = [toshkentvilregion, data2, data3, data9, gaz, svet, suv, kanal, data10, document,
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
        await state.set_state(ToshkentVilYerSotish.check)


@toshvil_yer_router.message(ToshkentVilYerSotish.check)
async def check(message: types.Message, state: FSMContext, bot: Bot):
    mycheck = message.text
    chat_id = message.chat.id

    media_group = MediaGroupBuilder()

    if mycheck == "✅ Эълонни жойлаш":
        data = await state.get_data()
        photos = data['images']

        if data['qoshimchaMalumot'] == "⏭️ Кейингиси" and data['telNumberTwo'] == "⏭️ Кейингиси":
            data3 = "♦️ Умумий майдон: " + data['umumiyMaydon'] + "-сотих" + "\n"
            data9 = "♦️ "
            gaz = data['gaz']
            svet = data['svet']
            suv = data['suv']
            kanal = data['kanal']
            data10 = " бор\n"
            document = "♦️ Ҳужжатлари: " + data['hujjatlar'] + "\n\n"
            data12 = "💲 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data13 = "📌 Манзил: " + data['manzil'] + "\n"
            data14 = "📌 Мўлжал: " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"

            result = [toshkentvilregion, data2, data3, data9, gaz, svet, suv, kanal, data10, document,
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

            await bot.send_message(chat_id=group_id, text="Буйруқ Беринг", reply_markup=toshvil_group)
            await bot.send_message(chat_id=chat_id, text=success_text, reply_markup=start, parse_mode="HTML")
            await state.clear() 

        elif data['qoshimchaMalumot'] == "⏭️ Кейингиси":
            data3 = "♦️ Умумий майдон: " + data['umumiyMaydon'] + "-сотих" + "\n"
            data9 = "♦️ "
            gaz = data['gaz']
            svet = data['svet']
            suv = data['suv']
            kanal = data['kanal']
            data10 = " бор\n"
            document = "♦️ Ҳужжатлари: " + data['hujjatlar'] + "\n\n"
            data12 = "💲 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data13 = "📌 Манзил: " + data['manzil'] + "\n"
            data14 = "📌 Мўлжал: " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
            data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"

            result = [toshkentvilregion, data2, data3, data9, gaz, svet, suv, kanal, data10, document,
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

            await bot.send_message(chat_id=group_id, text="Буйруқ Беринг", reply_markup=toshvil_group)
            await bot.send_message(chat_id=chat_id, text=success_text, reply_markup=start, parse_mode="HTML")
            await state.clear() 
        elif data["telNumberTwo"] == "⏭️ Кейингиси":
            data3 = "♦️ Умумий майдон: " + data['umumiyMaydon'] + "-сотих" + "\n"
            data9 = "♦️ "
            gaz = data['gaz']
            svet = data['svet']
            suv = data['suv']
            kanal = data['kanal']
            data10 = " бор\n"
            document = "♦️ Ҳужжатлари: " + data['hujjatlar'] + "\n"
            data11 = "♦️ Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n\n"
            data12 = "💲 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data13 = "📌 Манзил: " + data['manzil'] + "\n"
            data14 = "📌 Мўлжал: " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"

            result = [toshkentvilregion, data2, data3, data9, gaz, svet, suv, kanal, data10, document,
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

            await bot.send_message(chat_id=group_id, text="Буйруқ Беринг", reply_markup=toshvil_group)
            await bot.send_message(chat_id=chat_id, text=success_text, reply_markup=start, parse_mode="HTML")
            await state.clear() 
        else:
            data3 = "♦️ Умумий майдон: " + data['umumiyMaydon'] + "-сотих" + "\n"
            data9 = "♦️ "
            gaz = data['gaz']
            svet = data['svet']
            suv = data['suv']
            kanal = data['kanal']
            data10 = " бор\n"
            document = "♦️ Ҳужжатлари: " + data['hujjatlar'] + "\n"
            data11 = "♦️ Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n\n"
            data12 = "💲 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data13 = "📌 Манзил: " + data['manzil'] + "\n"
            data14 = "📌 Мўлжал: " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
            data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"

            result = [toshkentvilregion, data2, data3, data9, gaz, svet, suv, kanal, data10, document,
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

            await bot.send_message(chat_id=group_id, text="Буйруқ Беринг", reply_markup=toshvil_group)
            await bot.send_message(chat_id=chat_id, text=success_text, reply_markup=start, parse_mode="HTML")
            await state.clear() 
    if mycheck == "❌ Эълонни қайтадан ёзиш":
        await bot.send_message(chat_id=chat_id, text="<b>❌ Эълон қабул қилинмади</b>", parse_mode="HTML")
        await bot.send_message(chat_id=chat_id, text="<b>Еълон бериш учун қайтадан уриниб кўринг</b>", reply_markup=start, parse_mode="HTML")
        await state.clear()


@toshvil_yer_router.callback_query(IsGroupCall(), TasdiqlashToshvil.filter(F.word == "toshviltasdiqlash"))
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

    await bot.send_media_group(chat_id=toshvil_id, media=media_group.build())
    await bot.send_message(chat_id=int(data['user_id']), text=success_message)
    await bot.send_message(chat_id=call.message.chat.id, text=success_message)
    


@toshvil_yer_router.callback_query(IsGroupCall(), BekorQilishToshvil.filter(F.word=="toshvilbekor"))
async def dokumentlar(call: types.CallbackQuery, state: FSMContext):

    chat_id = str(call.message.message_id - 1)


    data = await db.yer_get_one_user_data(message_id=chat_id)

    await bot.send_message(chat_id=int(data['user_id']), text=fail_message)
    await bot.send_message(chat_id=call.message.chat.id, text=fail_message)