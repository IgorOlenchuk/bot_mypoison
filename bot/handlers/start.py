from aiogram.dispatcher.router import Router
from aiogram.types import Message
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from messages_data import message as mes
from keyboards.reply_kb import keyboard_main_menu


router = Router()


@router.message(Command("start"))
async def cmd_start(m: Message, state: FSMContext):
    await m.answer(text=mes.main.format(username=m.from_user.full_name), reply_markup=keyboard_main_menu())
