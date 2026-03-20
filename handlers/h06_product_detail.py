from aiogram import Router, F, Bot
from aiogram.types import FSInputFile, CallbackQuery

from bot_utils.message_uitils import text_for_caption
from database.utils import db_get_product_by_id, db_get_user_cart, db_add_or_update_item, db_get_all_category
from keyboards.inline import generate_category_menu, quantity_cart_controls
from keyboards.reply import phone_kb

router = Router()


@router.callback_query(F.data.startswith("product_view"))
async def show_product_detail(callback: CallbackQuery, bot: Bot):
    """Показ информации о проудукте"""
    chat_id = callback.message.chat.id
    message_id = callback.message.message_id

    await bot.delete_message(chat_id=chat_id, message_id=message_id)

    product_id = int(callback.data.split("_")[-1])
    product = db_get_product_by_id(product_id)
    user_cart = db_get_user_cart(chat_id)

    if user_cart:
        db_add_or_update_item(
            cart_id = user_cart.id,
            product_id = product.id,
            product_name = product.product_name,
            product_price = product.price,
            increment = 1
        )

        caption = text_for_caption(
            name = product.product_name,
            description = product.description,
            base_price = float(product.price),
        )

        product_image = FSInputFile(path = product.image)

        await bot.send_photo(
            chat_id=chat_id,
            photo=product_image,
            caption = caption,
            parse_mode = "HTML",
            reply_markup= quantity_cart_controls()
        )

    else:
         await ask_for_phone(chat_id, bot)

async def ask_for_phone(chat_id: int, bot: Bot):
    """Запрос номера телефона пользователя при отсутствии авторизации"""
    await bot.send_message(chat_id=chat_id, text= "Предоставте свой номер для оформления заказа",
                           reply_markup= phone_kb())


@router.callback_query(F.data == "from_detail_to_category")
async def handle_back_to_category(callback: CallbackQuery, bot: Bot):
    """Возврат в меню категорий из детальной карточки товара"""
    chat_id = callback.message.chat.id
    message_id = callback.message.message_id
    try:
        await bot.delete_message(chat_id=chat_id, message_id=message_id)

    except Exception as e :
        print(f"Сообщение не найдено, ошибка : {e}")

    categories = db_get_all_category()

    if not categories:
        await bot.send_message(chat_id= chat_id,
                               text= "Категории не найдены.")
        return
    keyboard = generate_category_menu(chat_id)
    await bot.send_message(chat_id= chat_id,
                           text="Выберите нужную вам категорию",
                           reply_markup=keyboard)
    await callback.answer()