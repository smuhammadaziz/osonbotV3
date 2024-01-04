from MediaGroup import AlbumMiddleware
from handlers.user.start import user_router
from handlers.user.UyJoyHandler import uyJoy_router


# hovli
from handlers.user.HovliSotish.AndijonHandler import andijon_router
from handlers.user.HovliSotish.BuxoroHandler import buxoro_router
from handlers.user.HovliSotish.FargonaHandler import fargona_router
from handlers.user.HovliSotish.JizzaxHandler import jizzax_router
from handlers.user.HovliSotish.NamanganHandler import namangan_router
from handlers.user.HovliSotish.NavoiyHandler import navoiy_router
from handlers.user.HovliSotish.QashqadaryoHandler import qashqa_router
from handlers.user.HovliSotish.QoraqalpoqHandler import qoraqalpoq_router
from handlers.user.HovliSotish.SamarqandHandler import samarqand_router
from handlers.user.HovliSotish.SirdaryoHandler import sirdaryo_router
from handlers.user.HovliSotish.SurxondaryoHandler import surxon_router
from handlers.user.HovliSotish.ToshkentShHandler import toshsh_router
from handlers.user.HovliSotish.ToshkentVilHandler import toshvil_router
from handlers.user.HovliSotish.XorazmHandler import xorazm_router

from aiogram import Router
from typing import NoReturn, List

routers: List[Router] = [user_router, uyJoy_router, andijon_router, buxoro_router, \
    fargona_router, jizzax_router, namangan_router, navoiy_router, qashqa_router, \
    qoraqalpoq_router, samarqand_router, sirdaryo_router, surxon_router, toshsh_router, \
    toshvil_router, xorazm_router]




def register_handlers(main_router: Router) -> NoReturn:
    for router in routers:
        main_router.include_router(router)
