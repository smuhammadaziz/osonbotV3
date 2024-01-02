from aiogram.fsm.state import State, StatesGroup


class ToshkentshHomeSotish(StatesGroup):
    images = State()
    umumiyMaydon = State()
    xonalar = State()
    qavat = State()
    qavatlik = State()
    remont = State()
    jihozlar = State()
    gaz = State()
    svet = State()
    suv = State()
    qoshimchaMalumot = State()
    valyuta = State()
    narxi = State()
    manzil = State()
    moljal = State()
    telNumberOne = State()
    telNumberTwo = State()
    check = State()
