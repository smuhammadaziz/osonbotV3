from typing import List

from aiogram import types, F, Router

from aiogram.types import Message

from aiogram.fsm.context import FSMContext

from keyboards.default.JobButton import checkbtn, start
from keyboards.default.JobButton import otkazishButton
from keyboards.inline.HomeButton import remontButton, jihozlarButton, valyutaButton, borYoq
from loader import bot
from states.HovliState.AndijonState import AndijonHomeSotishHovli

from transliterate import to_cyrillic

from utils.QuestionHovli.hovliqs import hovlitanlandi, rasmlar, umumiyMaydonyoz, faqatRaqamyoz, gazyoz, \
    jihozlaryoz, kanalizatsiyayoz, manzilyoz, moljalyoz, narxiyoz, nechaQavatyoz,oshxonayoz, \
    qoshimchaMalumotyoz, remontyoz, suvyoz, svetyoz, telraqam1yoz, telraqam2yoz, valyutayoz, \
    xammomyoz, xonalaryoz, channel_id, check_text, data1, data2, data30, data31, data32, data33, \
    data34, data35, success_text


mode = "Markdown"


andijon_router = Router()

@andijon_router.callback_query(F.text=="andijonhovli", state=None)
async def first(callback_query: types.CallbackQuery):
    await callback_query.answer("Kvartira tanlandi")
    await callback_query.message.answer("<b> Расмларни жойлаш (2 - 10  тагача) </b>", parse_mode="HTML")
    await AndijonHomeSotishHovli.images.set()


@andijon_router.message(is_media_group=True, state=AndijonHomeSotishHovli.images, content_types=types.ContentTypes.ANY)
async def starter(message: types.Message, album: List[types.Message], state: FSMContext):
    file_ids = []

    for photo in album:
        if photo:
            file_id = photo.photo[-1].file_id
            file_ids.append(file_id)

    await state.update_data({
        "images": file_ids
    })

    await message.answer("<b> Умумий майдонини ёзинг </b>", parse_mode="HTML")
    await AndijonHomeSotishHovli.next()


@andijon_router.message(lambda message: not message.text.replace('.', '').replace(',', '').isdigit(),
                    state=AndijonHomeSotishHovli.umumiyMaydon)
async def check_umumiy(message: types.Message):
    await message.reply("❗ Фақат рақамда ёзинг")


@andijon_router.message(state=AndijonHomeSotishHovli.umumiyMaydon)
async def umumiymaydon(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "umumiyMaydon": text
    })

    await bot.send_message(chat_id=message.chat.id, text="<b> Хоналар сонини ёзинг: </b>", parse_mode="HTML")
    await AndijonHomeSotishHovli.next()


@andijon_router.message(lambda message: not message.text.isdigit(), state=AndijonHomeSotishHovli.xonalar)
async def check_umumiy(message: types.Message):
    await message.reply("❗ Фақат рақамда ёзинг")


@andijon_router.message(state=AndijonHomeSotishHovli.xonalar)
async def umumiymaydon(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "xonalar": text
    })

    await bot.send_message(chat_id=message.chat.id, text="<b> Ошхона борми?  </b>", parse_mode="HTML",
                           reply_markup=borYoq)
    await AndijonHomeSotishHovli.next()


# =================================================
@andijon_router.callback_query(text='bor', state=AndijonHomeSotishHovli.oshxona)
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext):
    text = "бор"
    await callback_query.answer("Pressed")
    await state.update_data({
        "oshxona": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="Ҳаммоми борми?",
                           reply_markup=borYoq)
    await AndijonHomeSotishHovli.next()


@andijon_router.callback_query(text='yoq', state=AndijonHomeSotishHovli.oshxona)
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext):
    text = "йўқ"
    await callback_query.answer("Pressed")
    await state.update_data({
        "oshxona": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="Ҳаммоми борми?",
                           reply_markup=borYoq)
    await AndijonHomeSotishHovli.next()


@andijon_router.callback_query(text='bor', state=AndijonHomeSotishHovli.hammom)
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext):
    text = "бор"
    await callback_query.answer("Pressed")
    await state.update_data({
        "hammom": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="Неча қаватлик?")
    await AndijonHomeSotishHovli.next()


@andijon_router.callback_query(text='yoq', state=AndijonHomeSotishHovli.hammom)
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext):
    text = "йўқ"
    await callback_query.answer("Pressed")
    await state.update_data({
        "hammom": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="Неча қаватлик?")
    await AndijonHomeSotishHovli.next()


# ==============================================================


@andijon_router.message(lambda message: not message.text.isdigit(), state=AndijonHomeSotishHovli.qavat)
async def check_umumiy(message: types.Message):
    await message.reply("❗ Фақат рақамда ёзинг")


@andijon_router.message(state=AndijonHomeSotishHovli.qavat)
async def umumiymaydon(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "qavat": text
    })

    await bot.send_message(chat_id=message.chat.id, text="<b> Ремонти қандай?  </b>", parse_mode="HTML",
                           reply_markup=remontButton)
    await AndijonHomeSotishHovli.next()


# ====================================================================
@andijon_router.callback_query(text='Evroremont', state=AndijonHomeSotishHovli.remont)
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext):
    text = "Евроремонт"
    await callback_query.answer("Pressed")
    await state.update_data({
        "remont": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text="Жиҳозлари борми?",
                           reply_markup=jihozlarButton)
    await AndijonHomeSotishHovli.next()


@andijon_router.callback_query(text="Ta'mirlangan", state=AndijonHomeSotishHovli.remont)
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext):
    text = "Таъмирланган"
    await callback_query.answer("Pressed")
    await state.update_data({
        "remont": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text="Жиҳозлари борми?",
                           reply_markup=jihozlarButton)
    await AndijonHomeSotishHovli.next()


@andijon_router.callback_query(text="O'rtacha", state=AndijonHomeSotishHovli.remont)
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext):
    text = "Ўртача"
    await callback_query.answer("Pressed")
    await state.update_data({
        "remont": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text="Жиҳозлари борми?",
                           reply_markup=jihozlarButton)
    await AndijonHomeSotishHovli.next()


@andijon_router.callback_query(text="Ta'mirsiz", state=AndijonHomeSotishHovli.remont)
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext):
    text = "Таъмирсиз"
    await callback_query.answer("Pressed")
    await state.update_data({
        "remont": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text="Жиҳозлари борми?",
                           reply_markup=jihozlarButton)
    await AndijonHomeSotishHovli.next()


# ===============================================================

@andijon_router.callback_query(text='Mavjud', state=AndijonHomeSotishHovli.jihozlar)
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext):
    text = "бор"
    await callback_query.answer("Pressed")
    await state.update_data({
        "jihozlar": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="🔥 Газ борми?",
                           reply_markup=borYoq)
    await AndijonHomeSotishHovli.next()


@andijon_router.callback_query(text='Jihozlarsiz', state=AndijonHomeSotishHovli.jihozlar)
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext):
    text = "йўқ"
    await callback_query.answer("Pressed")
    await state.update_data({
        "jihozlar": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="🔥 Газ борми?",
                           reply_markup=borYoq)
    await AndijonHomeSotishHovli.next()


# ================================================================

@andijon_router.callback_query(text="bor", state=AndijonHomeSotishHovli.gaz)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext):
    text = "Газ ✔️"
    await callback_query.answer("Танланди")

    await state.update_data({
        "gaz": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text="💡 Свет борми?", reply_markup=borYoq)
    await AndijonHomeSotishHovli.next()


@andijon_router.callback_query(text="yoq", state=AndijonHomeSotishHovli.gaz)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext):
    text = "doesnotexist"
    await callback_query.answer("Танланди")

    await state.update_data({
        "gaz": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text="💡 Свет борми?", reply_markup=borYoq)
    await AndijonHomeSotishHovli.next()

    # ========================================================================


@andijon_router.callback_query(text="bor", state=AndijonHomeSotishHovli.svet)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext):
    text = "Свет ✔️"
    await callback_query.answer("Танланди")

    await state.update_data({
        "svet": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text="💦 Сув борми?", reply_markup=borYoq)
    await AndijonHomeSotishHovli.next()


@andijon_router.callback_query(text="yoq", state=AndijonHomeSotishHovli.svet)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext):
    text = "doesnotexist"
    await callback_query.answer("Танланди")

    await state.update_data({
        "svet": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text="💦 Сув борми?", reply_markup=borYoq)
    await AndijonHomeSotishHovli.next()


# ============================================================================

@andijon_router.callback_query(text="bor", state=AndijonHomeSotishHovli.suv)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext):
    text = "Сув ✔️"
    await callback_query.answer("Tanlandi")

    await state.update_data({
        "suv": text
    })

    await callback_query.message.answer(
        text="Канализация борми?",
        reply_markup=borYoq)

    await AndijonHomeSotishHovli.next()


@andijon_router.callback_query(text="yoq", state=AndijonHomeSotishHovli.suv)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext):
    text = "doesnotexist"
    await callback_query.answer("Tanlandi")

    await state.update_data({
        "suv": text
    })

    await callback_query.message.answer(
        text="Канализация борми?",
        reply_markup=borYoq)

    await AndijonHomeSotishHovli.next()


@andijon_router.callback_query(text="bor", state=AndijonHomeSotishHovli.kanal)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext):
    text = "Канализация  ✔️"
    await callback_query.answer("Tanlandi")

    await state.update_data({
        "kanal": text
    })

    await callback_query.message.answer(
        text="Қўшимча маълумотингиз бўлса,  ёзишингиз мумкин.  \n\n Йўқ бўлса 'Кейингиси' тугмасини босинг",
        reply_markup=otkazishButton)

    if callback_query.message.text == "⏭️ Кейингиси":
        await state.update_data({
            "qoshimchaMalumot": ""
        })
        await AndijonHomeSotishHovli.next()
    else:
        await AndijonHomeSotishHovli.next()


@andijon_router.callback_query(text="yoq", state=AndijonHomeSotishHovli.kanal)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext):
    text = "doesnotexist"
    await callback_query.answer("Tanlandi")

    await state.update_data({
        "kanal": text
    })

    await callback_query.message.answer(
        text="Қўшимча маълумотингиз бўлса,  ёзишингиз мумкин.  \n\n Йўқ бўлса 'Кейингиси' тугмасини босинг",
        reply_markup=otkazishButton)

    if callback_query.message.text == "⏭️ Кейингиси":
        await state.update_data({
            "qoshimchaMalumot": ""
        })
        await AndijonHomeSotishHovli.next()
    else:
        await AndijonHomeSotishHovli.next()


# ==============================================================

@andijon_router.message(state=AndijonHomeSotishHovli.qoshimchaMalumot)
async def umumiyMaydon(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "qoshimchaMalumot": text
    })
    await message.answer(text="Қайси валютада нарх белгиламоқчисиз?",
                         reply_markup=valyutaButton)

    await AndijonHomeSotishHovli.next()


# ==========================================

@andijon_router.callback_query(text='USD', state=AndijonHomeSotishHovli.valyuta)
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext):
    text = " $"
    await callback_query.answer("Pressed")

    await state.update_data({
        "valyuta": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text="Нархини ёзинг: ")

    await AndijonHomeSotishHovli.next()


@andijon_router.callback_query(text='SUM', state=AndijonHomeSotishHovli.valyuta)
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext):
    text = " сўм"
    await callback_query.answer("Pressed")

    await state.update_data({
        "valyuta": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text="Нархини ёзинг: ")

    await AndijonHomeSotishHovli.next()


# =================================

@andijon_router.message(lambda message: not message.text.isdigit(), state=AndijonHomeSotishHovli.narxi)
async def check_umumiy(message: types.Message):
    await message.reply("❗ Фақат рақамда ёзинг")


@andijon_router.message(state=AndijonHomeSotishHovli.narxi)
async def kvartira_narxi(message: types.Message, state: FSMContext):
    msg = int(message.text)

    number = "{:,}".format(msg).replace(",", ".")

    await state.update_data({
        "narxi": number
    })
    await message.answer(text="Манзилни ёзинг: ")

    await AndijonHomeSotishHovli.next()


@andijon_router.message(state=AndijonHomeSotishHovli.manzil)
async def umumiyMaydon(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "manzil": text
    })
    await message.answer(text="Мўлжални ёзинг: ")

    await AndijonHomeSotishHovli.next()


@andijon_router.message(state=AndijonHomeSotishHovli.moljal)
async def umumiyMaydon(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "moljal": text
    })
    await message.answer(text="Телефон рақамини ёзинг: ")

    await AndijonHomeSotishHovli.next()


@andijon_router.message(state=AndijonHomeSotishHovli.telNumberOne)
async def umumiyMaydon(message: types.Message, state: FSMContext):
    telNumber = message.text

    await state.update_data({
        "telNumberOne": telNumber
    })

    await message.answer(text="Зарур бўлса 2-рақамни киритинг,  \n\n  ёки 'Кейингиси'  тугмасини босинг",
                         reply_markup=otkazishButton)
    if message.text == "⏭️ Кейингиси":
        await state.update_data({
            "telNumberTwo": ""
        })
        await AndijonHomeSotishHovli.next()
    else:
        await AndijonHomeSotishHovli.next()


@andijon_router.message(state=AndijonHomeSotishHovli.telNumberTwo)
async def umumiyMaydon(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "telNumberTwo": text
    })

    chat_id = message.chat.id
    media_group = types.MediaGroup()

    data = await state.get_data()

    photos = data['images']

    
    if data['qoshimchaMalumot'] == "⏭️ Кейингиси" and data['telNumberTwo'] == "⏭️ Кейингиси":
        data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "-сотих" + "\n"
        data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
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
        data10 = "бор \n\n"
        data12 = "💰 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
        data13 = "📌 Манзил: " + data['manzil'] + "\n"
        data14 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
        data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"

        result = [data1, data2, data3, data4, oshxona, hammom, data6, data7, data8, data9, gaz, svet, suv, kanal,
                  data10,
                  data12, data13, data14, data15]

        array = []

        for item in result:
            if item == "doesnotexist":
                continue

            array.append(item)

        stringify = " ".join(array)
        cyrillic_text = to_cyrillic(stringify)

        media_group.attach_photo(photos[0], caption=cyrillic_text)

        for file_id in photos[1:]:
            media_group.attach_photo(f"{file_id}")

        await bot.send_media_group(chat_id=chat_id, media=media_group)
        await bot.send_message(chat_id=chat_id, text=check_text, reply_markup=checkbtn)
        await AndijonHomeSotishHovli.next()
    elif data['qoshimchaMalumot'] == "⏭️ Кейингиси":
        data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "-сотих" + "\n"
        data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
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
        data10 = "бор \n\n"
        data12 = "💰 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
        data13 = "📌 Манзил: " + data['manzil'] + "\n"
        data14 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
        data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
        data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"

        result = [data1, data2, data3, data4, oshxona, hammom, data6, data7, data8, data9, gaz, svet, suv, kanal,
                  data10,
                  data12, data13, data14, data15, data16]

        array = []

        for item in result:
            if item == "doesnotexist":
                continue

            array.append(item)

        stringify = " ".join(array)
        cyrillic_text = to_cyrillic(stringify)

        media_group.attach_photo(photos[0], caption=cyrillic_text)

        for file_id in photos[1:]:
            media_group.attach_photo(f"{file_id}")

        await bot.send_media_group(chat_id=chat_id, media=media_group)
        await bot.send_message(chat_id=chat_id, text=check_text, reply_markup=checkbtn)
        await AndijonHomeSotishHovli.next()

    elif data['telNumberTwo'] == "⏭️ Кейингиси":
        data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "-сотих" + "\n"
        data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
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
        data10 = "бор \n"
        data11 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n\n"
        data12 = "💰 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
        data13 = "📌 Манзил: " + data['manzil'] + "\n"
        data14 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
        data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"

        result = [data1, data2, data3, data4, oshxona, hammom, data6, data7, data8, data9, gaz, svet, suv, kanal,
                  data10,
                  data11, data12, data13, data14, data15]

        array = []

        for item in result:
            if item == "doesnotexist":
                continue

            array.append(item)

        stringify = " ".join(array)
        cyrillic_text = to_cyrillic(stringify)

        media_group.attach_photo(photos[0], caption=cyrillic_text)

        for file_id in photos[1:]:
            media_group.attach_photo(f"{file_id}")

        await bot.send_media_group(chat_id=chat_id, media=media_group)
        await bot.send_message(chat_id=chat_id, text=check_text, reply_markup=checkbtn)
        await AndijonHomeSotishHovli.next()

    else:
        data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "-сотих" + "\n"
        data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
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
        data10 = "бор \n"
        data11 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n\n"
        data12 = "💰 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
        data13 = "📌 Манзил: " + data['manzil'] + "\n"
        data14 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
        data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
        data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"

        result = [data1, data2, data3, data4, oshxona, hammom, data6, data7, data8, data9, gaz, svet, suv, kanal,
                  data10,
                  data11, data12, data13, data14, data15, data16]

        array = []

        for item in result:
            if item == "doesnotexist":
                continue

            array.append(item)

        stringify = " ".join(array)
        cyrillic_text = to_cyrillic(stringify)

        media_group.attach_photo(photos[0], caption=cyrillic_text)

        for file_id in photos[1:]:
            media_group.attach_photo(f"{file_id}")

        await bot.send_media_group(chat_id=chat_id, media=media_group)
        await bot.send_message(chat_id=chat_id, text=check_text, reply_markup=checkbtn)
        await AndijonHomeSotishHovli.next()


@andijon_router.message(state=AndijonHomeSotishHovli.check)
async def check(message: types.Message, state: FSMContext):
    mycheck = message.text
    chat_id = message.chat.id

    media_group = types.MediaGroup()

    if mycheck == "✅ Эълонни жойлаш":
        data = await state.get_data()
        photos = data['images']

        if data['qoshimchaMalumot'] == "⏭️ Кейингиси" and data['telNumberTwo'] == "⏭️ Кейингиси":
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "-сотих" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
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
            data10 = "бор \n\n"
            data12 = "💰 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data13 = "📌 Манзил: " + data['manzil'] + "\n"
            data14 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"

            result = [data1, data2, data3, data4, oshxona, hammom, data6, data7, data8, data9, gaz, svet, suv, kanal,
                      data10,
                      data12, data13, data14, data15]

            array = []

            for item in result:
                if item == "doesnotexist":
                    continue

                array.append(item)

            stringify = " ".join(array)
            cyrillic_text = to_cyrillic(stringify)+data30+data31+data32+data33+data34+data35

            media_group.attach_photo(photos[0], caption=cyrillic_text, parse_mode="HTML")

            for file_id in photos[1:]:
                media_group.attach_photo(f"{file_id}")

            await bot.send_media_group(chat_id=channel_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=success_text, reply_markup=start)
            await state.finish()

        elif data['qoshimchaMalumot'] == "⏭️ Кейингиси":
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "-сотих" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
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
            data10 = "бор \n\n"
            data12 = "💰 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data13 = "📌 Манзил: " + data['manzil'] + "\n"
            data14 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
            data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"

            result = [data1, data2, data3, data4, oshxona, hammom, data6, data7, data8, data9, gaz, svet, suv, kanal,
                      data10,
                      data12, data13, data14, data15, data16]

            array = []

            for item in result:
                if item == "doesnotexist":
                    continue

                array.append(item)

            stringify = " ".join(array)
            cyrillic_text = to_cyrillic(stringify)+data30+data31+data32+data33+data34+data35

            media_group.attach_photo(photos[0], caption=cyrillic_text, parse_mode="HTML")

            for file_id in photos[1:]:
                media_group.attach_photo(f"{file_id}")

            await bot.send_media_group(chat_id=channel_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=success_text, reply_markup=start)
            await state.finish()
        elif data["telNumberTwo"] == "⏭️ Кейингиси":
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "-сотих" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
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
            data10 = "бор \n"
            data11 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n\n"
            data12 = "💰 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data13 = "📌 Манзил: " + data['manzil'] + "\n"
            data14 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"

            result = [data1, data2, data3, data4, oshxona, hammom, data6, data7, data8, data9, gaz, svet, suv, kanal,
                      data10,
                      data11, data12, data13, data14, data15]

            array = []

            for item in result:
                if item == "doesnotexist":
                    continue

                array.append(item)

            stringify = " ".join(array)
            cyrillic_text = to_cyrillic(stringify)+data30+data31+data32+data33+data34+data35

            media_group.attach_photo(photos[0], caption=cyrillic_text, parse_mode="HTML")

            for file_id in photos[1:]:
                media_group.attach_photo(f"{file_id}")

            await bot.send_media_group(chat_id=channel_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=success_text, reply_markup=start)
            await state.finish()
        else:
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "-сотих" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
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
            data10 = "бор \n"
            data11 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n\n"
            data12 = "💰 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data13 = "📌 Манзил: " + data['manzil'] + "\n"
            data14 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
            data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"

            result = [data1, data2, data3, data4, oshxona, hammom, data6, data7, data8, data9, gaz, svet, suv, kanal,
                      data10,
                      data11, data12, data13, data14, data15, data16]

            array = []

            for item in result:
                if item == "doesnotexist":
                    continue

                array.append(item)

            stringify = " ".join(array)
            cyrillic_text = to_cyrillic(stringify)+data30+data31+data32+data33+data34+data35

            media_group.attach_photo(photos[0], caption=cyrillic_text, parse_mode="HTML")

            for file_id in photos[1:]:
                media_group.attach_photo(f"{file_id}")

            await bot.send_media_group(chat_id=channel_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=success_text, reply_markup=start)
            await state.finish()

    if mycheck == "❌ Эълонни қайтадан ёзиш":
        await bot.send_message(chat_id=chat_id, text="❌ Эълон қабул қилинмади")
        await bot.send_message(chat_id=chat_id, text="Еълон бериш учун қайтадан уриниб кўринг", reply_markup=start)
        await state.finish()
