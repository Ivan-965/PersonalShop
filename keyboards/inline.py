from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from database.utils import db_get_all_category, db_get_finally_price, db_get_products

"""Модуль с функцими для создания inline клавиатур"""


def generate_category_menu(chat_id):
    """inline клавиатура с категориями товаров"""
    categories = db_get_all_category()
    total_price = db_get_finally_price(chat_id)

    builder = InlineKeyboardBuilder()
    builder.button(
        text=f'Корзина заказа ({total_price if total_price else 0} рублей)',
        callback_data='Корзина заказа'
    )

    [builder.button(text=category.category_name, callback_data=f'category_{category.id}')
     for category in categories]

    builder.adjust(1, 2)
    return builder.as_markup()


def show_product_by_category(category_id: int):
    """кнопка для показа продуктов по категориям"""
    products = db_get_products(category_id)
    builder = InlineKeyboardBuilder()
    [builder.button(text=product.product_name, callback_data=f'product_view_{product.id}') for product in products]
    builder.adjust(2)
    builder.row(
        InlineKeyboardButton(text="🔙 Назад", callback_data='return_to_category')
    )
    return builder.as_markup()


def quantity_cart_controls(quantity=1):
    """Кнопка для изменения количества товара"""
    builder = InlineKeyboardBuilder()
    builder.button(text="➖", callback_data="action -")
    builder.button(text=str(quantity), callback_data="quantity")
    builder.button(text="➕", callback_data="action +")
    builder.button(text="Добавить в коризину", callback_data="положить в корзину")
    builder.button(text="🔙 Назад", callback_data="from_detail_to_category")
    builder.adjust(3, 1, 1)

    return builder.as_markup(resize_keyboard=True)


def cart_actions_kb():
    """Оформление заказа, добавление и удаление из корзины."""
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="Оформить заказ!📦", callback_data="confirm_order"),
        InlineKeyboardButton(text= "Удалить товары.🗑️", callback_data="remove_item"),
        InlineKeyboardButton(text= "Добавить товар.®️", callback_data="add_item")
        )
    builder.adjust(1,2)
    return builder.as_markup(resize_keyboard=True)