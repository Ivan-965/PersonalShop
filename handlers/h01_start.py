from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, FSInputFile

from database.utils import db_register_user
from keyboards.reply import start_kb, phone_kb

router = Router()


@router.message(CommandStart())
async def command_start(message: Message):
    """Handler for /start command"""

    photo = FSInputFile("media/apple.jpg")
    await message.answer_photo(
        photo=photo,
        caption=f"Добрый день, <i>{message.from_user.full_name}</i>\nНажмите кнопку ниже,чтобы начать",
        parse_mode='HTML',
        reply_markup=start_kb()
    )


@router.message(F.text == "Зайти в магазин 🏪")
async def handle_start_button(message: Message):
    """ Handler for 'start button' """
    await handle_start(message)


async def handle_start(message: Message):
    """Вызов функции регистрации пользователя"""
    await register_user(message)


async def register_user(message: Message):
    """Регистрация пользователя"""
    chat_id = message.chat.id
    full_name = message.from_user.full_name

    if db_register_user(chat_id, full_name):
        await message.answer(text="Добро пожаловать в магазин!")
        await show_main_menu(message)

    else:
        await message.answer(text="Для работы с ботом необходимо зарегистрироваться", reply_markup=phone_kb())