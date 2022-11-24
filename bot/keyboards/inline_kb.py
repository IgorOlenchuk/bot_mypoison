from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from messages_data import message as mes


def keyboard_instruction() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    sizes = (1, 1)
    builder.button(text=mes.instruction, url=mes.url_instruction)
    builder.adjust(*sizes)
    return builder.as_markup(resize_keyboard=True)


def keyboard_instruction_read() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    sizes = (1, 1)
    builder.button(text=mes.instruction_manual_read, url=mes.url_instruction)
    builder.adjust(*sizes)
    return builder.as_markup(resize_keyboard=True)


def rate_info() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    sizes = (1, 1)
    builder.button(text=mes.rate_info, url=mes.url_rate)
    builder.adjust(*sizes)
    return builder.as_markup(resize_keyboard=True)


def preorder() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    sizes = (1, 1)
    builder.button(text=mes.pre_order_btn, callback_data=mes.pre_order_btn)
    builder.adjust(*sizes)
    return builder.as_markup(resize_keyboard=True)
