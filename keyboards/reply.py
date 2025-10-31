from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, ReplyKeyboardMarkup


def start_kb():
    """Start keyboard."""
    return ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text="Зайти в магазин 🏪")]],
            resize_keyboard=True
    )
