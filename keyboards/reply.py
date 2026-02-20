from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, ReplyKeyboardMarkup
"""Модуль для формирования кнопок меню. Типа reply"""


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


def get_main_menu():
    """Формирование кнопок меню."""
    builder = ReplyKeyboardBuilder()
    builder.button(text= "Оформить заказ ✅")
    builder.button(text= "История 📃")
    builder.button(text= "Корзина 🛒")
    builder.button(text= "Настройки ⚙️")
    builder.adjust(2, 2)
    return builder.as_markup(resize_keyboard=True)

def back_to_main_menu():
    """Кнопка возврата в главное меню."""
    builder = ReplyKeyboardBuilder()
    builder.button(text="Главное меню🏠")
    return builder.as_markup(resize_keyboard=True)

def arrow_back_button():
    """Стрелочка назад к предыдущему шагу диалоговоего процесса."""
    builder = ReplyKeyboardBuilder()
    builder.button(text= "Назад🔙")
    return builder.as_markup(resize_keyboard=True)