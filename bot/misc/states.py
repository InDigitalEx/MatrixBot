from typing import Final

from aiogram.dispatcher.filters.state import StatesGroup, State


class MatrixState(StatesGroup):
    NAME: Final = State()
    DATE: Final = State()
    GENDER: Final = State()
