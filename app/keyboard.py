from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог')],
    [KeyboardButton(text='Корзина'), KeyboardButton(text='Контакты')]
], resize_keyboard=True, input_field_placeholder="Выберите пункт меню.")

second = InlineKeyboardMarkup( inline_keyboard=[
    [InlineKeyboardButton(text='Каталог', callback_data='catalog')],
    [InlineKeyboardButton(text='Корзина', callback_data='cart')],
    [InlineKeyboardButton(text='Контакты', callback_data='contacts')],
])

settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Youtube', url='https://youtube.com/@oleg_kishinsky')]
])

test_buttons = ['YouTube', 'Linkedin', 'Twitter']

async def start_keyboard():
    keyboard = InlineKeyboardBuilder()
    for button in test_buttons:
        keyboard.add(InlineKeyboardButton(text=button, url="https://t.me/oleg_kishinsky"))
    return keyboard.adjust(2).as_markup()