from aiogram.fsm.state import StatesGroup, State

class States(StatesGroup):
    weather = State()
    currency = State()
    ip = State()