import asyncio
import logging
import sys
import functools
from dotenv import load_dotenv
import os

load_dotenv()


from aiogram import Bot, Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from app.apsched import message_admin
from app.handler import router


async def on_startup(bot):
    scheduler = AsyncIOScheduler()
    scheduler.add_job(functools.partial(message_admin, bot), 'cron', hour=6, minute=0)
    scheduler.start()


async def main():
    bot = Bot(token=os.getenv('BOT_TOKEN'))
    dp = Dispatcher()
    dp.include_router(router)
    dp.startup.register(on_startup)

    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == '__main__':
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Выход из бота')
