
import asyncio

from aiogram import Bot, Dispatcher
from handlers.process_handlers import router
from config.config import load_config
from db.db_funcs import db_conn


async def main():

    config = load_config()
    
    bot = Bot(token=config.tgbot.token)
    dp = Dispatcher()
    dp.include_router(router)
    await db_conn()
    await dp.start_polling(bot)


asyncio.run(main())
