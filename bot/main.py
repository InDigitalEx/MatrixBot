"""
Matrix of Destiny Bot
"""
from loguru import logger

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from bot.misc import Env
from bot.handlers import register_all_handlers


async def __on_start_up(dp: Dispatcher) -> None:
    logger.info('Bot starts')

    register_all_handlers(dp)


def start_telegram_bot() -> None:
    bot = Bot(token=Env.TOKEN, parse_mode='HTML')
    dp = Dispatcher(bot, storage=MemoryStorage())
    executor.start_polling(dp, skip_updates=True, on_startup=__on_start_up)
