from aiogram.fsm.state import State, StatesGroup


class GoodsForm(StatesGroup):
    start = State()
    count = State()
    cost = State()
    next_link = State()
    link = State()
    send = State()
    size = State()
    accept = State()


class GoodsForm_2(StatesGroup):
    start = State()
    count = State()
    cost = State()
    next_link = State()
    link = State()
    send = State()
    size = State()
    accept = State()