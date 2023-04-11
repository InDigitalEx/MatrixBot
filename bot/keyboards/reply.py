from typing import Final
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


KB_MAIN: Final = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
KB_MAIN.add(KeyboardButton(text="Разбор матрицы ✡️"),
            KeyboardButton(text="Инфо 📌"),
            KeyboardButton(text="Техподдержка ⚙"))

KB_GENDER: Final = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
KB_GENDER.add(KeyboardButton(text="Женский"),
              KeyboardButton(text="Мужской"))
