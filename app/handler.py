import asyncio
import json
import sched
import time

from aiogram import Router, F, Bot
from aiogram.filters import CommandStart, Filter
from aiogram.types import Message, CallbackQuery

import app.weather as weather
import app.keyboards as kb

router = Router()


class Admin(Filter):
    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in [415131308]


@router.message(Admin(), F.text == '/admin')
async def cmd_admin(message: Message):
    await message.answer('Вы админ')


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Добро пожаловать', reply_markup=kb.main)


@router.message(F.text == 'Мой профиль')
async def cmd_start(message: Message):
    await message.answer(f'Имя - {message.from_user.first_name} \n chat id ={message.chat.id}', reply_markup=kb.main)


@router.message(F.text == 'Каталог')
async def cmd_start(message: Message):
    await message.delete()
    await message.answer('asdf', reply_markup=kb.catalog)


@router.message(F.text == 'Погода')
async def cmd_start(message: Message):
    await message.answer(await weather.get_weather())


@router.callback_query(F.data == 'adidas')
async def adidas(callback: CallbackQuery):
    await callback.answer(f'Вы выбрали adidas')


@router.message(F.location)
async def adidas(message: Message):
    await message.answer(f'opop geo?')
    print(f'added new geo - {message.location}')


@router.message()
async def echo(message: Message):
    await message.reply(f'а? что ты имел ввиду?')
