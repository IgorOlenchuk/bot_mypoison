import os


from aiogram.types import Message
from aiogram.filters import Text
from aiogram.dispatcher.router import Router

from keyboards.reply_kb import keyboard_main_menu
from keyboards.inline_kb import keyboard_instruction_read, rate_info
from messages_data import message as mes
from utils.rate import rate
from utils import config


router = Router()


@router.message(Text(text=mes.yuan_exchange_rate_btn))
async def course_uany(m: Message):
    await m.answer(text=mes.rate.format(rate=rate(config.VALUTE)), disable_web_page_preview=True, reply_markup=rate_info())


@router.message(Text(text=mes.delivery_btn))
async def delivery(m: Message):
    await m.answer(text=mes.delivery_text, disable_web_page_preview=True, reply_markup=keyboard_main_menu())


@router.message(Text(text=mes.instruction_manual_btn))
async def instuction(m: Message):
    await m.answer(text=mes.instruction_manual_text, disable_web_page_preview=True, reply_markup=keyboard_instruction_read())


@router.message(Text(text=mes.support_btn))
async def support(m: Message):
    await m.answer(text=mes.support_text, disable_web_page_preview=True, reply_markup=keyboard_main_menu())
