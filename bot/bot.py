import os
import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from handlers import start, order, menu, preorder
from utils import config


logging.basicConfig(level=logging.INFO)


def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=config.TELEGRAM_TOKEN, parse_mode="HTML")
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(start.router)
    dp.include_router(order.router)
    dp.include_router(preorder.router)
    dp.include_router(menu.router)
    dp.run_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
