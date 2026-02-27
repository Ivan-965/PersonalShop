from aiogram import Router, F, Bot
from aiogram.types import FSInputFile, CallbackQuery

from database.utils import db_get_product_by_id
from keyboards.inline import generate_category_menu

router = Router()

@router.callback_query(F.data.startswith("product_view"))
async def show_product_detail(callback: CallbackQuery, bot: Bot):
    """Показ информации о проудукте"""
    chat_id = callback.message.chat.id
    message_id = callback.message.message_id

    await bot.delete_message(chat_id= chat_id, message_id= message_id)

    product_id = int(callback.data.split("_")[-1])
    product = db_get_product_by_id(product_id)