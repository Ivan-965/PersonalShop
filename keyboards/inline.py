from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

"""Модуль с функцими для создания inline клавиатур"""


def generate_category_menu(chat_id):
    """Генерация меню категорий"""
    categories = db_get_all_categories()
    total_price = db_get_finally_price(chat_id)

    builder = InlineKeyboardBuilder()
    builder.button(
        text=f"Корзина заказа ({total_price if total_price else 0}рублей)",
        сallback_data="Корзина заказа"
    )

    [builder.button(text=category.category_name, callback_data=f'category_{category.id}')
    for category in categories]
    builder.adjust(1, 2)
    return builder.as_markup(resize_keyboard=True)