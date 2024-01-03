from handlers.user.start import user_router
from handlers.user.echo import echo_router
from handlers.user.UyJoyHandler import uyJoy_router
from handlers.user.HovliSotish.AndijonHandler import andijon_router

from aiogram import Router
from typing import NoReturn, List

routers: List[Router] = [user_router, echo_router, uyJoy_router, andijon_router]


def register_handlers(main_router: Router) -> NoReturn:
    for router in routers:
        main_router.include_router(router)
