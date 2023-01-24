from aiogram.dispatcher.router import Router
from aiogram.types import Message
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from keyboards.reply_kb import keyboard_main_menu
from aiogram import types 
from messages_data import message as mes
from utils.utils import post_data, get_data
from utils import config

router = Router()

DB_API_URL = config.DB_API_URL


@router.message(Command("start"))
async def cmd_start(m: Message):
    try:
        url = f'{DB_API_URL}users/{m.from_user.id}'
        user = await get_data(url)
        if user['is_banned'] == False:
            await m.answer(text=mes.main.format(username=m.from_user.full_name), reply_markup=keyboard_main_menu())
        else:
            await m.answer(text='Извините, вы не допущены к использованию бота', reply_markup=types.ReplyKeyboardRemove())
    except:
        url = f'{DB_API_URL}users/'
        await post_data(url=url, json={ 
            "id": m.from_user.id,
            "tg_name": m.from_user.full_name,
            "first_name": m.from_user.first_name,
            "last_name": m.from_user.last_name
        })
        await m.answer(text=mes.main.format(username=m.from_user.full_name), reply_markup=keyboard_main_menu())
