from aiogram import Dispatcher, Bot, types
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from bot.keyboards import KB_MAIN, KB_GENDER
from bot.misc import Messages
from bot.misc import MatrixState
from bot.parser import get_matrix_photo, delete_matrix_temp


async def __matrix_parsing(msg: Message, state: FSMContext) -> None:
    await msg.answer(Messages.MSG_MATRIX_NAME, reply_markup=ReplyKeyboardRemove())
    await state.set_state(MatrixState.NAME)


async def __matrix_parsing_name(msg: Message, state: FSMContext) -> None:
    await state.update_data(name=msg.text)
    await msg.answer(Messages.MSG_MATRIX_DATE)
    await state.set_state(MatrixState.DATE)


async def __matrix_parsing_date(msg: Message, state: FSMContext) -> None:
    await state.update_data(date=msg.text)
    await msg.answer(Messages.MSG_MATRIX_GENDER, reply_markup=KB_GENDER)
    await state.set_state(MatrixState.GENDER)


async def __matrix_parsing_gender(msg: Message, state: FSMContext) -> None:
    await state.update_data(gender=msg.text)
    await msg.answer(Messages.MSG_MATRIX_DONE, reply_markup=ReplyKeyboardRemove())

    data = await state.get_data()
    await msg.answer_photo(get_matrix_photo(data['name'], data['date'], data['gender']), reply_markup=KB_MAIN)
    await delete_matrix_temp()
    await state.finish()


def _register_matrix_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(__matrix_parsing, content_types=['text'], text='Разбор матрицы ✡️')
    dp.register_message_handler(__matrix_parsing_name, content_types=['text'], state=MatrixState.NAME)
    dp.register_message_handler(__matrix_parsing_date, content_types=['text'], state=MatrixState.DATE)
    dp.register_message_handler(__matrix_parsing_gender, content_types=['text'], state=MatrixState.GENDER)
