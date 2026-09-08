from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from keyboards.inline import get_settings_menu
from keyboards.reply import get_main_menu

router = Router()

@router.message(F.text == "Настройки ⚙️")
async def handle_settings_menu(message: Message):
    """Обработка настроек"""
    await message.answer("Настройки🔧", reply_markup=get_settings_menu())

@router.callback_query(F.data == "back_to_menu")
async def handle_back_to_menu(callback: CallbackQuery):
    """Выход назад из меню настроек"""
    await callback.message.delete()
    await callback.message.answer("Главное меню", reply_markup=get_main_menu())
