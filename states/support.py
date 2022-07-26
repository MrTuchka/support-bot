from aiogram.dispatcher.filters.state import StatesGroup, State


class support(StatesGroup):
    in_call = State()
    ready_to_call = State()