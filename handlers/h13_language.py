from aiogram import Router, F
from aiogram.types import CallbackQuery, ReplyKeyboardRemove

from database.utils import db_update_language
from keyboards.inline import get_language_keyboard, get_settings_menu

router = Router()

@router.callback_query(F.data == "change_language")
async def change_language(callback: CallbackQuery):
    """смена языка"""
    await callback.message.edit_text(text="Сменить язык: ", reply_markup=get_language_keyboard())


@router.callback_query(F.data.startwith("lang_"))
async def set_language(callback: CallbackQuery):
    """сменя языка и сохранение данных бд"""

    new_lang = callback.data.split("_")[1]
    telegram_id = callback.from_user.id
    db_update_language(telegram_id, new_lang)

    text = "✅Язык успешно изменён на русский " if new_lang == "ru" else "✅Language successfully changed to English"
    await callback.message.edit_text(text=text, reply_markup=get_settings_menu())