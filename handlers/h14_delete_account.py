from aiogram import Router, F, Bot
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import CallbackQuery

from config import MANAGER_ID
from keyboards.inline import delete_account_kb, get_settings_menu
from keyboards.reply import start_kb
from database.utils import db_delete_user_by_telegram_id

router = Router()

@router.callback_query(F.data == "delete_account")
async def handle_delete_account(callback: CallbackQuery):
    """запрос на удаление аккаунта"""
    await callback.message.edit_text("вы уверенны что хотите удалить аккаунт?\n\nданные будут удаленны",
                                     reply_markup=delete_account_kb())


@router.callback_query(F.data == "confirm_delete")
async def handle_confirm_delete(callback: CallbackQuery, bot: Bot):
    """ подтверждение удаления аккаунта """
    telegram_id = callback.from_user.id
    full_name = callback.from_user.full_name

    success = db_delete_user_by_telegram_id(telegram_id)

    if success:
        try:
            await callback.message.delete()
        except TelegramBadRequest:
            pass

        await callback.message.answer(
            f" аккаунт {full_name} удален, для повторной работы необходимо авторизоваться снова ",
            reply_markup=start_kb())
        await bot.send_message(MANAGER_ID, f" аккаунт {full_name} с телеграм id {telegram_id} был удален ")

    else:
        await callback.message.edit_text("ошибка удаления аккаунта, попробуйте еще раз", reply_markup=get_settings_menu())