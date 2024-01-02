from aiogram import types, Router, F

from keyboards.default.JobButton import button
from keyboards.inline.HomeButton import allRegionsKvartira, toshkentShHome, toshkentVilHome, \
    andijonHome, namanganHome, fargonaHome, samarqandHome, buxoroHome, sirdaryoHome, qashqadaryoHome, \
    surxonHome, navoiyHome, jizzaxHome, xorazmHome, qoraqalpoqHome

from loader import bot

from aiogram.types.callback_query import CallbackQuery

from keyboards.inline.data import AndijonData, BuxoroData, FargonaData, JizzaxData, NamanganData, \
    NavoiyData, QashqadaryoData, QoraqalpoqData, SamarqandData, SirdaryoData, SurxondaryoData, \
    toshkentshData, toshkentvilData, XorazmData

mode = "Markdown"

uyJoy_router = Router() 


# =======================================1=======================================
@uyJoy_router.callback_query(AndijonData.filter(F.word=="andijon"), F.chat_type=="private")
async def kvartirasotish(call: CallbackQuery, callback_data: AndijonData):
    await call.answer("Andijon tanlandi")
    await call.message.answer("<b> Уй-жой турини танланг!  </b>", reply_markup=andijonHome, parse_mode="HTML")

# =======================================2========================================
@uyJoy_router.callback_query(BuxoroData.filter(F.word=="buxoro"), F.chat_type=="private")
async def kvartirasotish(call: CallbackQuery, callback_data: BuxoroData):
    await call.answer("Buxoro tanlandi")
    await call.message.answer("<b> Уй-жой турини танланг!  </b>", reply_markup=buxoroHome, parse_mode="HTML")

# =======================================3========================================
@uyJoy_router.callback_query(FargonaData.filter(F.word=="fargona"), F.chat_type=="private")
async def kvartirasotish(call: CallbackQuery, callback_data: FargonaData):
    await call.answer("Farg'ona tanlandi")
    await call.message.answer("<b> Уй-жой турини танланг!  </b>", reply_markup=fargonaHome, parse_mode="HTML")

# =======================================4========================================
@uyJoy_router.callback_query(JizzaxData.filter(F.word=="jizzax"), F.chat_type=="private")
async def kvartirasotish(call: CallbackQuery, callback_data: JizzaxData):
    await call.answer("Jizzax tanlandi")
    await call.message.answer("<b> Уй-жой турини танланг!  </b>", reply_markup=jizzaxHome, parse_mode="HTML")

# =======================================5========================================
@uyJoy_router.callback_query(NamanganData.filter(F.word=="namangan"), F.chat_type=="private")
async def kvartirasotish(call: CallbackQuery, callback_data: NamanganData):
    await call.answer("Namangan tanlandi")
    await call.message.answer("<b> Уй-жой турини танланг!  </b>", reply_markup=namanganHome, parse_mode="HTML")

# =======================================6========================================
@uyJoy_router.callback_query(NavoiyData.filter(F.word=="navoiy"), F.chat_type=="private")
async def kvartirasotish(call: CallbackQuery, callback_data: NavoiyData):
    await call.answer("Navoiy tanlandi")
    await call.message.answer("<b> Уй-жой турини танланг!  </b>", reply_markup=navoiyHome, parse_mode="HTML")

# =======================================7========================================
@uyJoy_router.callback_query(QashqadaryoData.filter(F.word=="qashqa"), F.chat_type=="private")
async def kvartirasotish(call: CallbackQuery, callback_data: QashqadaryoData):
    await call.answer("Qashqadaryo tanlandi")
    await call.message.answer("<b> Уй-жой турини танланг!  </b>", reply_markup=qashqadaryoHome, parse_mode="HTML")

# =======================================8========================================
@uyJoy_router.callback_query(QoraqalpoqData.filter(F.word=="qora"), F.chat_type=="private")
async def kvartirasotish(call: CallbackQuery, callback_data: QoraqalpoqData):
    await call.answer("Qoraqalpog'iston tanlandi")
    await call.message.answer("<b> Уй-жой турини танланг!  </b>", reply_markup=qoraqalpoqHome, parse_mode="HTML")

# =======================================9========================================
@uyJoy_router.callback_query(SamarqandData.filter(F.word=="samarqand"), F.chat_type=="private")
async def kvartirasotish(call: CallbackQuery, callback_data: SamarqandData):
    await call.answer("Samarqand tanlandi")
    await call.message.answer("<b> Уй-жой турини танланг!  </b>", reply_markup=samarqandHome, parse_mode="HTML")

# =======================================10========================================
@uyJoy_router.callback_query(SirdaryoData.filter(F.word=="sirdaryo"), F.chat_type=="private")
async def kvartirasotish(call: CallbackQuery, callback_data: SirdaryoData):
    await call.answer("Sirdaryo tanlandi")
    await call.message.answer("<b> Уй-жой турини танланг!  </b>", reply_markup=sirdaryoHome, parse_mode="HTML")

# =======================================11========================================
@uyJoy_router.callback_query(SurxondaryoData.filter(F.word=="surxon"), F.chat_type=="private")
async def kvartirasotish(call: CallbackQuery, callback_data: SurxondaryoData):
    await call.answer("Surxondaryo tanlandi")
    await call.message.answer("<b> Уй-жой турини танланг!  </b>", reply_markup=surxonHome, parse_mode="HTML")

# =======================================12========================================
@uyJoy_router.callback_query(toshkentshData.filter(F.word=="toshkent"), F.chat_type=="private")
async def kvartirasotish(call: CallbackQuery, callback_data: toshkentshData):
    await call.answer("Toshkent Shahar tanlandi")
    await call.message.answer("<b> Уй-жой турини танланг!  </b>", reply_markup=toshkentShHome, parse_mode="HTML")

# =======================================13========================================
@uyJoy_router.callback_query(toshkentvilData.filter(F.word=="toshkentvil"), F.chat_type=="private")
async def kvartirasotish(call: CallbackQuery, callback_data: toshkentvilData):
    await call.answer("Toshkent Viloyati tanlandi")
    await call.message.answer("<b> Уй-жой турини танланг!  </b>", reply_markup=toshkentVilHome, parse_mode="HTML")

# =======================================14========================================
@uyJoy_router.callback_query(XorazmData.filter(F.word=="xorazm"), F.chat_type=="private")
async def kvartirasotish(call: CallbackQuery, callback_data: XorazmData):
    await call.answer("Xorazm tanlandi")
    await call.message.answer("<b> Уй-жой турини танланг!  </b>", reply_markup=xorazmHome, parse_mode="HTML")

# ===================================--finish--=====================================

