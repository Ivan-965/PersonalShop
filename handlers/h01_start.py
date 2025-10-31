from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, FSInputFile

from keyboards.reply import start_kb

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


@router.message(F.text == "зайти в магазин 🏪")
async def handle_start_button(message: Message):
    """ Handler for 'start button' """
    await handle_start(message)


async def handle_start(message: Message):
    """ Handler for /start command """
    await register_user(message)


async def register_user(message: Message):
    pass
