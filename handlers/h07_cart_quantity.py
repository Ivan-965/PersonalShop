from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery

from database.utils import db_get_product_by_name, db_get_user_cart
from keyboards.inline import quantity_cart_controls

router = Router()

@router.callback_query(F.data.regexp(r"^action [+-]"))
async def change_product_quantity(callback: CallbackQuery, bot: Bot):
    """Изменяем количество товара в корзине"""
    chat_id = callback.from_user.id
    message_id = callback.message.message_id
    action = callback.data.split()[-1]

    product_name = callback.message.caption.split("\n")[0]
    product = db_get_product_by_name(product_name)
    cart = db_get_user_cart(chat_id)


    if not product or not cart:
        await callback.answer("Товар или крозина не найдена.")
        return

    increment = 1 if action == "+" else -1