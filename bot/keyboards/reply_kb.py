from aiogram.types import ReplyKeyboardMarkup 
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from messages_data import message as mes


def keyboard_main_menu() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    sizes = (2, 3, 1)
    builder.button(text=mes.place_an_order_btn)
    builder.button(text=mes.price_calculator_btn)
    builder.button(text=mes.yuan_exchange_rate_btn)
    builder.button(text=mes.delivery_btn)
    builder.button(text=mes.instruction_manual_btn)
    builder.button(text=mes.support_btn)
    builder.adjust(*sizes)
    return ReplyKeyboardMarkup(keyboard=builder.export(), resize_keyboard=True)


def keyboard_order() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    sizes = (1, 2)
    builder.button(text=mes.continue_btn)
    builder.button(text=mes.back_btn)
    builder.button(text=mes.main_menu_btn)
    builder.adjust(*sizes)
    return ReplyKeyboardMarkup(keyboard=builder.export(), resize_keyboard=True)


def keyboard_agree() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    sizes = (1, 2)
    builder.button(text=mes.agree_btn)
    builder.button(text=mes.back_btn)
    builder.button(text=mes.main_menu_btn)
    builder.adjust(*sizes)
    return ReplyKeyboardMarkup(keyboard=builder.export(), resize_keyboard=True)


def keyboard_order_accept() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    sizes = (1, 2)
    builder.button(text=mes.send_btn)
    builder.button(text=mes.cancel_btn)
    builder.adjust(*sizes)
    return ReplyKeyboardMarkup(keyboard=builder.export(), resize_keyboard=True)


def keyboard_cancel() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    sizes = (1, 2)
    builder.button(text=mes.cancel_btn)
    builder.adjust(*sizes)
    return ReplyKeyboardMarkup(keyboard=builder.export(), resize_keyboard=True)
