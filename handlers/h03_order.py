from aiogram import Router, F, Bot
from aiogram.filters import CommandStart
from aiogram.types import Message, FSInputFile

from database.utils import db_get_last_orders
from keyboards.inline import generate_category_menu
from keyboards.reply import back_to_main_menu

"""Обработчик кнопки Оформить заказ и История"""

router = Router()


@router.message(F.text == "Оформить заказ ✅")
async def make_order(message: Message, bot: Bot):
    """Оброботка кнопки Оформить заказ с дальнейшим переходом в котегории товаров"""
    chat_id = message.chat.id
    await bot.send_message(chat_id, "Переходим...", reply_markup=back_to_main_menu())
    await message.answer(text="Выберете категорию:", reply_markup=generate_category_menu(chat_id))


@router.message(F.text == "История 📃")
async def order_history(message: Message):
    """Демонстрация последних 5 заказов"""
    chat_id = message.chat.id
    orders = db_get_last_orders(chat_id)
    if not orders:
        await message.answer("У вас нет заказов😭")
        return

    text = "Последние 5 заказов📋:\n\n"
    for item in orders:
        order = item["order"]

        line_price = float(order.final_price)
        text += f"{order.product_name} - {order.quantity}шт. - {line_price}₽\n\n"

    await message.answer(text)