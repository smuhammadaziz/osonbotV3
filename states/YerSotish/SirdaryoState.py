from aiogram.fsm.state import State, StatesGroup


class SirdaryoYerSotish(StatesGroup):
    images = State()
    umumiyMaydon = State()
    gaz = State()
    svet = State()
    suv = State()
    kanal = State()
    qoshimchaMalumot = State()
    hujjatlar = State()
    valyuta = State()
    narxi = State()
    manzil = State()
    moljal = State()
    telNumberOne = State()
    telNumberTwo = State()
    check = State()
