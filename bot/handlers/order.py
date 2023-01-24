import os
import requests

from aiogram import Bot, F
from aiogram.types import Message
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.dispatcher.router import Router

from keyboards.reply_kb import keyboard_main_menu, keyboard_order, keyboard_cancel, keyboard_order_accept, keyboard_agree
from keyboards.inline_kb import keyboard_instruction
from messages_data import message as mes
from fsm_states_groups import GoodsForm
from utils import config
from utils.utils import get_data, post_data
from utils.rate import rate
from utils.settings import settings, comission, rate


router = Router()
bot = Bot(token=config.TELEGRAM_TOKEN, parse_mode="HTML")
DB_API_URL = config.DB_API_URL


@router.message(Text(text=mes.place_an_order_btn))
async def order(m: Message, state: FSMContext):
    await m.answer(text=mes.place_an_order_btn, reply_markup=keyboard_order())
    await m.answer(text=mes.order, reply_markup=keyboard_instruction())
    await state.set_state(GoodsForm.start)


@router.message(GoodsForm.start, Text(text=mes.back_btn))
async def order_back(m: Message, state: FSMContext):
    await state.clear()
    await m.answer(text=mes.main_menu_btn, reply_markup=keyboard_main_menu())


@router.message(GoodsForm.start, Text(text=mes.continue_btn))
async def countgoods(m: Message, state: FSMContext):
    await m.answer(text=mes.order_count, reply_markup=keyboard_cancel())
    await state.set_state(GoodsForm.count)


@router.message(GoodsForm.start, Text(text=mes.main_menu_btn))
async def order_mmenu(m: Message, state: FSMContext):
    await state.clear()
    await m.answer(text=mes.main_menu_btn, reply_markup=keyboard_main_menu())


@router.message(GoodsForm.count, Text(text=mes.cancel_btn))
async def order_cancel(m: Message, state: FSMContext):
    await state.clear()
    await order(m, state)


@router.message(GoodsForm.count)
async def costgoods(m: Message, state: FSMContext):
    count=m.text
    if count.isdigit() == True and int(count)!=0:
        await state.update_data(count=m.text)        
    else:
        await m.answer(text=mes.error, reply_markup=keyboard_cancel())
        await m.answer(text=mes.error_again, reply_markup=keyboard_cancel())
        return
    await state.set_state(GoodsForm.cost)
    await m.answer(text=mes.order_cost, disable_web_page_preview=True, reply_markup=keyboard_cancel())


@router.message(GoodsForm.cost, Text(text=mes.cancel_btn))
async def order_cancel(m: Message, state: FSMContext):
    await state.clear()
    await order(m, state)


@router.message(GoodsForm.cost)
async def linksgoods(m: Message, state: FSMContext):
    cost=m.text
    if cost.isdigit() == True and int(cost)!=0:
        await state.update_data(cost=m.text)        
    else:
        await m.answer(text=mes.error, reply_markup=keyboard_cancel())
        await m.answer(text=mes.error_again, reply_markup=keyboard_cancel())
        return
    data = await state.get_data()
    r = await rate(valute=config.VALUTE)
    total = await settings(valute=config.VALUTE, cost=data['cost'], count=data['count'])
    com = await comission()
    await m.answer(text=mes.order_calc.format(total=total, rate=r, comission=com), reply_markup=keyboard_order())
    await state.set_state(GoodsForm.next_link)


@router.message(GoodsForm.next_link, Text(text=mes.continue_btn))
async def costgoods(m: Message, state: FSMContext):
    await m.answer(text=mes.order_continue, disable_web_page_preview=True, reply_markup=keyboard_order_accept())
    await state.set_state(GoodsForm.link)


@router.message(GoodsForm.link, Text(text=mes.cancel_btn))
async def order_cancel(m: Message, state: FSMContext):
    await state.clear()
    await order(m, state)


@router.message(GoodsForm.link)
async def accept(m: Message, state: FSMContext):
    await state.update_data(link=m.text)
    data = await state.get_data()
    await m.answer(text=mes.order_accept, reply_markup=keyboard_order_accept())
    await state.set_state(GoodsForm.send)


@router.message(GoodsForm.send, Text(text=mes.cancel_btn))
async def order_cancel(m: Message, state: FSMContext):
    await state.clear()
    await order(m, state)


@router.message(GoodsForm.send, Text(text=mes.send_btn))
async def accept(m: Message, state: FSMContext):
    await m.answer(text=mes.size, disable_web_page_preview=True, reply_markup=keyboard_order_accept())
    await state.set_state(GoodsForm.size)


@router.message(GoodsForm.size, Text(text=mes.cancel_btn))
async def order_cancel(m: Message, state: FSMContext):
    await state.clear()
    await order(m, state)


@router.message(GoodsForm.size)
async def size(m: Message, state: FSMContext):
    await state.update_data(size=m.text)
    await m.answer(text=mes.agree, reply_markup=keyboard_agree())
    await state.set_state(GoodsForm.accept)


@router.message(GoodsForm.accept, Text(text=mes.agree_btn))
async def success_agree(m: Message, state: FSMContext):
    data = await state.get_data()
    r = await rate(valute=config.VALUTE)
    total = await settings(valute=config.VALUTE, cost=data['cost'], count=data['count'])
    url=f'{DB_API_URL}users/{m.from_user.id}/order/'
    await post_data(url=url, json={
        "user": m.from_user.id,
        "count": data['count'],
        "cost": data['cost'],
        "size": data['size'],
        "link": data['link'],
        "total_cost": int(total)}
        )
    respondents = await get_data(f'{DB_API_URL}users/respondents/')
    for id in respondents:
        await bot.send_message(id, text=mes.order_user.format(
            user=m.from_user.id,
            user_full=m.from_user.full_name,
            count=data['count'],
            cost=data['cost'],
            size=data['size'],
            link=data['link'],
            rate=r,
            total=total),
            parse_mode='HTML', disable_web_page_preview=True, reply_markup=keyboard_order_accept())
    await m.answer(text=mes.success_order, disable_web_page_preview=True, reply_markup=keyboard_main_menu())


@router.message(Text(text= mes.cancel_btn))
async def cancel(m: Message, state: FSMContext):    
    await state.clear()
    await order(m, state)


@router.message(Text(text=mes.back_btn))
async def order_back(m: Message, state: FSMContext):
    await state.clear()
    await order(m, state)


@router.message(Text(text=mes.main_menu_btn))
async def order_main(m: Message, state: FSMContext):
    await state.clear()
    await m.answer(text=mes.main_menu_btn, reply_markup=keyboard_main_menu())
