from aiogram import Dispatcher, Bot
from aiogram.types import Message


async def __other_messages(msg: Message) -> None:
    bot: Bot = msg.bot
    await bot.send_message(msg.from_user.id, "Неизвестная команда, напишите <b>/start</b>")


def register_other_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(__other_messages, content_types=['text'], state=None)
