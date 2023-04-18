from abc import ABC
from typing import Final

from aiogram.types import Message

from bot.misc.config import Config


class Messages(ABC):

    # Basic messages

    MSG_MATRIX_NAME: Final = "<b>Введите имя человека</b>"
    MSG_MATRIX_DATE: Final = "<b>Введите дату рождения в формате <i>01.01.2000</i></b>"
    MSG_MATRIX_DATE_ERROR: Final = "<b>Ошибка! Введите дату в формате <i>01.01.2000</i></b>"
    MSG_MATRIX_GENDER: Final = "<b>Выберите пол</b>"
    MSG_MATRIX_DONE: Final = "<b>Загрузка... ⏳⏳⏳</b>"

    # Static methods

    @staticmethod
    def get_bot_info(msg: Message) -> str:
        return f"Привет, <b>{msg.from_user.first_name}</b>! 🥳\n\n"\
               f"Это бот для отправки и расшифровки матрицы судьбы!"

    @staticmethod
    def get_bot_help(msg: Message) -> str:
        return f"<b>{msg.from_user.first_name}, данный раздел находится в разработке</b>"

    @staticmethod
    def get_bot_tech_support(msg: Message) -> str:
        return f"<b>{msg.from_user.first_name}, если у вас возникли проблемы, " \
               f"напишите нам - <i>{Config.HELPER_URL}</i></b>"
