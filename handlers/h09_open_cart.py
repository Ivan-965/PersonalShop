from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from database.utils import db_get_cart_items
from keyboards.inline import cart_actions_kb

router = Router()


@router.message(F.text == "Корзина 🛒")
async def handle_open_cart(message: Message):
    """Обработка реплай кнопки "коризна" """
    chat_id = message.chat.id
    await show_cart(chat_id=chat_id, send_fn=message.answer)


@router.callback_query(F.data == "Корзина заказа")
async def open_cart(callback: CallbackQuery):
    """Обработка инлан кнопки "Корзина заказа" """
    chat_id = callback.from_user.id
    await show_cart(chat_id=chat_id, send_fn=callback.message.answer)
    await callback.answer()

async def show_cart(chat_id: int, send_fn):
    """Показ содердимого корзины"""
    cart_items = db_get_cart_items(chat_id)

    if not cart_items:
        await send_fn("Ваша Корзинка пустая! Добавьте товары в нее.")
        return

    text = "Содержимое корзины📋:\n"
    total = 0

    for item in cart_items:
        total = float(item["final_price"]) + total
        text += f"{item["product_name"]} - {item["quantity"]}шт. - {item["final_price"]}₽\n"

    text += f"\nИтоговая сумма:{total}₽"
    await send_fn(text, reply_markup= cart_actions_kb())