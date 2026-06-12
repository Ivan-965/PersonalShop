from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

from database.utils import db_get_product_for_delete
from keyboards.inline import cart_actions_kb

router = Router()

@router.callback_query(F.data == "add_item")
async def choose_product_to_add(callback: CallbackQuery):
    """Обработка увеличения количества товара в корзине"""
    cart_products = db_get_product_for_delete(callback.from_user.id)
    builder = InlineKeyboardBuilder()
    for cart_id, name in cart_products:
        builder.button(text= f"➕ {name}", callback_data= f"increase_{cart_id}")
    builder.button(text="🔙 Назад", callback_data=f"back_to_cart_review")
    builder.adjust(1)

    await callback.message.edit_text(text='Выберите товар для увеличения', reply_markup=builder.as_markup())
    await callback.answer()

@router.callback_query(F.data == "remove_item")
async def choose_product_to_remove(callback: CallbackQuery):
    """Обработка уменьшения количества товара в корзине"""
    cart_products = db_get_product_for_delete(callback.from_user.id)
    builder = InlineKeyboardBuilder()
    for cart_id, name in cart_products:
        builder.button(text= f"➖ {name}", callback_data= f"decrease_{cart_id}")
    builder.button(text="🔙 Назад", callback_data=f"back_to_cart_review")
    builder.adjust(1)

    await callback.message.edit_text(text='Выберите товар для уменьшения', reply_markup=builder.as_markup())
    await callback.answer()

@router.callback_query(F.data == "back_to_cart_review")
async def back_to_cart(callback: CallbackQuery):
    """Возврат к просмотру товаров в корзине"""
    await callback.message.edit_text("Ваша корзина:", reply_markup=cart_actions_kb())
    await callback.answer()