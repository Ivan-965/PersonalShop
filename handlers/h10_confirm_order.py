from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery

from bot_utils.counting_products import counting_products
from config import MANAGER_ID
from database.utils import db_get_user_phone

router = Router()


@router.callback_query(F.data == "confirm_order")
async def confirm_order(callback: CallbackQuery, bot: Bot):
    """Подтверждение заказа"""

    user = callback.message.from_user
    phone = db_get_user_phone(user.id)
    mention = f"<a href='tg://user?id={user.id}'> {user.full_name}</a>"

    user_text = f"Новый заказ от {mention}\nТелефон:{phone}."
    context = counting_products(user.id, user_text)
    print("КОНТЕКС", context)

    if not context:
        await callback.message.edit_text("Корзина пустая!")
        await callback.answer()
        return

    if not MANAGER_ID:
        await callback.message.edit_text("Оформление заказа невозможно с пустой корзиной")
        await callback.answer()
        return

    count, text, tota_price, cart_id = context
    await bot.send_message(MANAGER_ID, text, parse_mode="HTML")
