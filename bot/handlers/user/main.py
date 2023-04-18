from aiogram import Dispatcher
from aiogram.types import Message

from bot.handlers.user.matrix import _register_matrix_handlers
from bot.keyboards import KB_MAIN
from bot.misc import Messages


async def __start(msg: Message) -> None:
    await msg.answer(Messages.get_bot_info(msg), reply_markup=KB_MAIN)


async def __info(msg: Message) -> None:
    await msg.answer(Messages.get_bot_help(msg))


async def __tech_support(msg: Message) -> None:
    await msg.answer(Messages.get_bot_tech_support(msg))


def register_user_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(__start, commands=['start'])
    dp.register_message_handler(__info, content_types=['text'], text='Инфо 📌')
    dp.register_message_handler(__tech_support, content_types=['text'], text='Техподдержка ⚙')

    _register_matrix_handlers(dp)
