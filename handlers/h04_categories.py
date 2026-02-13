from aiogram import F, Router
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import CallbackQuery, InlineKeyboardMarkup

from keyboards.inline import show_product_by_category

router = Router()


@router.callback_query(F.data.regexp(r"^category_(\d+)$"))
async def show_product(callback: CallbackQuery):
    """Показ всех товаров в выбранной категории"""
    chat_id = callback.message.chat.id
    message_id = callback.message.message_id
    category_id = int(callback.data.split("_")[-1])

    try:
        await callback.bot.edit_message_text(
            text="Выберите товар",
            chat_id=chat_id,
            message_id=message_id,
            reply_markup=show_product_by_category(category_id)
        )

    except TelegramBadRequest:
        await callback.answer("Не удалось открыть выбранную категорию")
