from aiogram import types, Router, F

from keyboards.default.JobButton import button
from keyboards.inline.HomeButton import allRegionsKvartira, toshkentShHome, toshkentVilHome, andijonHome, \
    namanganHome, \
    fargonaHome, samarqandHome, buxoroHome, sirdaryoHome, qashqadaryoHome, surxonHome, navoiyHome, jizzaxHome, \
    xorazmHome, qoraqalpoqHome
from loader import bot

mode = "Markdown"

uyJoy_router = Router()


# =======================================1=======================================
@uyJoy_router.callback_query(F.text=="andijon", F.chat_type=="private")
async def kvartirasotish(call: types.CallbackQuery):
    await call.answer("Andijon tanlandi")
    await call.message.answer("<b> Уй-жой турини танланг!  </b>", reply_markup=andijonHome, parse_mode="HTML")

# =======================================2========================================
@uyJoy_router.callback_query(F.text=="buxoro", F.chat_type=="private")
async def kvartirasotish(call: types.CallbackQuery):
    await call.answer("Buxoro tanlandi")
    await call.message.answer("<b> Уй-жой турини танланг!  </b>", reply_markup=buxoroHome, parse_mode="HTML")

# =======================================3========================================
@uyJoy_router.callback_query(F.text=="fargona", F.chat_type=="private")
async def kvartirasotish(call: types.CallbackQuery):
    await call.answer("Farg'ona tanlandi")
    await call.message.answer("<b> Уй-жой турини танланг!  </b>", reply_markup=fargonaHome, parse_mode="HTML")

# =======================================4========================================
@uyJoy_router.callback_query(F.text=="jizzax", F.chat_type=="private")
async def kvartirasotish(call: types.CallbackQuery):
    await call.answer("Jizzax tanlandi")
    await call.message.answer("<b> Уй-жой турини танланг!  </b>", reply_markup=jizzaxHome, parse_mode="HTML")

# =======================================5========================================
@uyJoy_router.callback_query(F.text=="namangan", F.chat_type=="private")
async def kvartirasotish(call: types.CallbackQuery):
    await call.answer("Namangan tanlandi")
    await call.message.answer("<b> Уй-жой турини танланг!  </b>", reply_markup=namanganHome, parse_mode="HTML")

# =======================================6========================================
@uyJoy_router.callback_query(F.text=="navoiy", F.chat_type=="private")
async def kvartirasotish(call: types.CallbackQuery):
    await call.answer("Navoiy tanlandi")
    await call.message.answer("<b> Уй-жой турини танланг!  </b>", reply_markup=navoiyHome, parse_mode="HTML")

# =======================================7========================================
@uyJoy_router.callback_query(F.text=="qashqadaryo", F.chat_type=="private")
async def kvartirasotish(call: types.CallbackQuery):
    await call.answer("Qashqadaryo tanlandi")
    await call.message.answer("<b> Уй-жой турини танланг!  </b>", reply_markup=qashqadaryoHome, parse_mode="HTML")

# =======================================8========================================
@uyJoy_router.callback_query(F.text=="qoraqalpoqosh", F.chat_type=="private")
async def kvartirasotish(call: types.CallbackQuery):
    await call.answer("Qoraqalpog'iston tanlandi")
    await call.message.answer("<b> Уй-жой турини танланг!  </b>", reply_markup=qoraqalpoqHome, parse_mode="HTML")

# =======================================9========================================
@uyJoy_router.callback_query(F.text=="samarqand", F.chat_type=="private")
async def kvartirasotish(call: types.CallbackQuery):
    await call.answer("Samarqand tanlandi")
    await call.message.answer("<b> Уй-жой турини танланг!  </b>", reply_markup=samarqandHome, parse_mode="HTML")

# =======================================10========================================
@uyJoy_router.callback_query(F.text=="sirdaryo", F.chat_type=="private")
async def kvartirasotish(call: types.CallbackQuery):
    await call.answer("Sirdaryo tanlandi")
    await call.message.answer("<b> Уй-жой турини танланг!  </b>", reply_markup=sirdaryoHome, parse_mode="HTML")

# =======================================11========================================
@uyJoy_router.callback_query(F.text=="surxondaryo", F.chat_type=="private")
async def kvartirasotish(call: types.CallbackQuery):
    await call.answer("Surxondaryo tanlandi")
    await call.message.answer("<b> Уй-жой турини танланг!  </b>", reply_markup=surxonHome, parse_mode="HTML")

# =======================================12========================================
@uyJoy_router.callback_query(F.text=="toshkentsh", F.chat_type=="private")
async def kvartirasotish(call: types.CallbackQuery):
    await call.answer("Toshkent Shahar tanlandi")
    await call.message.answer("<b> Уй-жой турини танланг!  </b>", reply_markup=toshkentShHome, parse_mode="HTML")

# =======================================13========================================
@uyJoy_router.callback_query(F.text=="toshkentvil", F.chat_type=="private")
async def kvartirasotish(call: types.CallbackQuery):
    await call.answer("Toshkent Viloyati tanlandi")
    await call.message.answer("<b> Уй-жой турини танланг!  </b>", reply_markup=toshkentVilHome, parse_mode="HTML")

# =======================================14========================================
@uyJoy_router.callback_query(F.text=="xorazm", F.chat_type=="private")
async def kvartirasotish(call: types.CallbackQuery):
    await call.answer("Xorazm tanlandi")
    await call.message.answer("<b> Уй-жой турини танланг!  </b>", reply_markup=xorazmHome, parse_mode="HTML")

# ===================================--finish--=====================================



