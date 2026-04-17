from aiogram import Router, F, Bot
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import CallbackQuery, InputMediaPhoto, FSInputFile, InlineKeyboardMarkup

from bot_utils.message_uitils import text_for_caption
from database.utils import db_get_product_by_name, db_get_user_cart, db_add_or_update_item
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

    result = db_add_or_update_item(
        cart_id = cart.id,
        product_id = product.id,
        product_name = product.product_name,
        product_price = product.price,
        increment = increment)

    if result["status"] == "error":
        await callback.answer("Ошибка при изменении количества.", show_alert=True)
        return

    caption = text_for_caption(
        name= product.product_name,
        description= product.description,
        base_price= float(product.price)*result["product_quantity"]
    )
    try:
        await bot.edit_message_media(
            chat_id = chat_id,
            message_id = message_id,
            media= InputMediaPhoto(
                media= FSInputFile(path= product.image),
                caption= caption,
                parse_mode= "HTML"
            ),
            reply_markup= quantity_cart_controls(result["product_quantity"])
        )

    except TelegramBadRequest:
        pass