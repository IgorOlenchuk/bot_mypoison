import os
import requests

from aiogram import Bot
from aiogram.types import CallbackQuery, Message
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.dispatcher.router import Router

from keyboards.reply_kb import keyboard_main_menu, keyboard_order, keyboard_cancel, keyboard_order_accept, keyboard_agree
from keyboards.inline_kb import keyboard_instruction, preorder
from messages_data import message as mes
from fsm_states_groups import GoodsForm_2
from utils import config
from utils.rate import rate
from utils.utils import get_data
from utils.settings import settings, comission, rate

router = Router()
bot = Bot(token=config.TELEGRAM_TOKEN, parse_mode="HTML")
DB_API_URL = config.DB_API_URL


@router.message(Text(text=mes.price_calculator_btn))
async def calc_price(m: Message, state: FSMContext):
    await m.answer(text=mes.order_count, reply_markup=keyboard_cancel())
    await state.set_state(GoodsForm_2.count)


@router.message(GoodsForm_2.count, Text(text=mes.cancel_btn))
async def order_cancel(m: Message, state: FSMContext):
    await state.clear()
    await order(m, state)


@router.message(GoodsForm_2.count)
async def costgoods(m: Message, state: FSMContext):
    count=m.text
    if count.isdigit() == True and int(count)!=0:
        await state.update_data(count=m.text)        
    else:
        await m.answer(text=mes.error, reply_markup=keyboard_cancel())
        await m.answer(text=mes.error_again, reply_markup=keyboard_cancel())
        return
    await state.set_state(GoodsForm_2.cost)
    await m.answer(text=mes.order_cost_2, disable_web_page_preview=True, reply_markup=keyboard_cancel())


@router.message(GoodsForm_2.cost, Text(text=mes.cancel_btn))
async def order_cancel(m: Message, state: FSMContext):
    await state.clear()
    await order(m, state)


@router.message(GoodsForm_2.cost)
async def linksgoods(m: Message, state: FSMContext):
    cost=m.text
    if cost.isdigit() == True and int(cost)!=0:
        await state.update_data(cost=m.text)        
    else:
        await m.answer(text=mes.error, reply_markup=keyboard_cancel())
        await m.answer(text=mes.error_again, reply_markup=keyboard_cancel())
        return
    data = await state.get_data()
    sum = await settings(valute=config.VALUTE, cost=data['cost'], count=data['count'])
    com = await comission()
    r = await rate(valute=config.VALUTE)
    await m.answer(text=mes.order_calc_2.format(sum=sum, p=int(data['cost']), c=int(data['count']), r=r, comission=com), reply_markup=keyboard_order())
    await state.set_state(GoodsForm_2.next_link)


@router.message(GoodsForm_2.next_link, Text(text=mes.continue_btn))
async def accept(m: Message, state: FSMContext):
    data = await state.get_data()
    await m.answer(text=mes.pre_order, reply_markup=preorder())


@router.callback_query(Text(text=mes.pre_order_btn))
async def accept(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text=mes.order_continue, disable_web_page_preview=True, reply_markup=keyboard_order_accept())
    await state.set_state(GoodsForm_2.link)

@router.message(GoodsForm_2.link, Text(text=mes.cancel_btn))
async def order_cancel(m: Message, state: FSMContext):
    await state.clear()
    await order(m, state)


@router.message(GoodsForm_2.link)
async def accept(m: Message, state: FSMContext):
    await state.update_data(link=m.text)
    await m.answer(text=mes.order_accept, reply_markup=keyboard_order_accept())
    await state.set_state(GoodsForm_2.send)


@router.message(GoodsForm_2.send, Text(text=mes.cancel_btn))
async def order_cancel(m: Message, state: FSMContext):
    await state.clear()
    await order(m, state)


@router.message(GoodsForm_2.send, Text(text=mes.send_btn))
async def accept(m: Message, state: FSMContext):
    await m.answer(text=mes.size, disable_web_page_preview=True, reply_markup=keyboard_order_accept())
    await state.set_state(GoodsForm_2.size)


@router.message(GoodsForm_2.size, Text(text=mes.cancel_btn))
async def order_cancel(m: Message, state: FSMContext):
    await state.clear()
    await order(m, state)


@router.message(GoodsForm_2.size)
async def size(m: Message, state: FSMContext):
    await state.update_data(size=m.text)
    await m.answer(text=mes.agree, reply_markup=keyboard_agree())
    await state.set_state(GoodsForm_2.accept)


@router.message(GoodsForm_2.accept, Text(text=mes.agree_btn))
async def success_agree(m: Message, state: FSMContext):
    data = await state.get_data()
    total = await settings(valute=config.VALUTE, cost=data['cost'], count=data['count'])
    r = await rate(valute=config.VALUTE)
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


@router.message(Text(text=mes.place_an_order_btn))
async def order(m: Message, state: FSMContext):
    await m.answer(text=mes.place_an_order_btn, reply_markup=keyboard_order())
    await m.answer(text=mes.order, reply_markup=keyboard_instruction())
    await state.set_state(GoodsForm_2.start)


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
