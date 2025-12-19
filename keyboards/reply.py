from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, ReplyKeyboardMarkup


def start_kb():
    """Start keyboard."""
    return ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text="Зайти в магазин 🏪")]],
            resize_keyboard=True
    )

def phone_kb():
    """кнопка для ввода телефона"""
    builder = ReplyKeyboardBuilder()
    builder.button(text='Отправьте ваш номер телефона', request_contact=True)
    return builder.as_markup(resize_keyboard=True)
