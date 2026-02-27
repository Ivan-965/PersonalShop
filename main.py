"""Главный файл проекта. В нём запускается бот."""
import asyncio
from aiogram import Bot, Dispatcher
from handlers import h01_start, h02_get_contact, h03_order, h04_categories, h05_navigation, h06_product_detail
from config import TOKEN


bot = Bot(token=TOKEN)

dp = Dispatcher()

dp.include_router(h01_start.router)
dp.include_router(h02_get_contact.router)
dp.include_router(h03_order.router)
dp.include_router(h04_categories.router)
dp.include_router(h05_navigation.router)
dp.include_router(h06_product_detail.router)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
