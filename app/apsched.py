from aiogram import Bot

from app import weather


async def message_admin(bot: Bot):
    await bot.send_message(415131308, await weather.get_weather())
