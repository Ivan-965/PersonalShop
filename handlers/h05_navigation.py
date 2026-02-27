from aiogram import Bot, Router, F
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import Message

from handlers.h03_order import make_order

router = Router()


@router.message(F.text == "Назад🔙")
async def return_to_back(message: Message, bot: Bot):
    """Возвращение назад и удаление последнего сообщения"""
    try:
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
    except TelegramBadRequest:
        pass

    await make_order(message, bot)

