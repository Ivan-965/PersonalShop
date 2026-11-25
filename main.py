"""Главный файл проекта. В нём запускается бот."""
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.telegram import TelegramAPIServer
# Имопрт для запуска бота из регионов с ограничениями
from aiogram.client.session.aiohttp import AiohttpSession

from handlers import h01_start, h02_get_contact, h03_order, h04_categories, h05_navigation, h06_product_detail, \
    h07_cart_quantity, h08_add_to_cart, h09_open_cart, h10_confirm_order, h11_cart_modify, h12_settings, h13_language
from config import TOKEN


WORKER_URL = "https://summer-bird-f441.skosiv13.workers.dev/"

api_server = TelegramAPIServer.from_base(WORKER_URL)
session = AiohttpSession(api=api_server)

bot = Bot(token=TOKEN, session=session)

dp = Dispatcher()

dp.include_router(h01_start.router)
dp.include_router(h02_get_contact.router)
dp.include_router(h03_order.router)
dp.include_router(h04_categories.router)
dp.include_router(h05_navigation.router)
dp.include_router(h06_product_detail.router)
dp.include_router(h07_cart_quantity.router)
dp.include_router(h08_add_to_cart.router)
dp.include_router(h09_open_cart.router)
dp.include_router(h10_confirm_order.router)
dp.include_router(h11_cart_modify.router)
dp.include_router(h12_settings.router)
dp.include_router(h13_language.router)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())