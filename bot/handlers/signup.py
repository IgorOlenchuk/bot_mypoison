import logging
from aiogram.dispatcher.router import Router
from aiogram.fsm.context import FSMContext
from utils.utils import post_data
from utils import config

router = Router()

DB_API_URL = config.DB_API_URL


async def start_register(m: Message, state: FSMContext):
    async with state.proxy() as data:
        url = f'{DB_API_URL}users/'
        await post_data(url=url, json={
            "id": message.from_user.id,
            "tg_name": message.from_user.full_name,
            "first_name": message.from_user.first_name,
            "last_name": message.from_user.last_name
        })
    await m.answer(text=mes.main.format(username=m.from_user.full_name), reply_markup=keyboard_main_menu())
