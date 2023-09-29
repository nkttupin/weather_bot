from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main_kb = [
    [KeyboardButton(text='Погода')],
    [KeyboardButton(text='Мой профиль'),
     KeyboardButton(text='Отправить ГЕО',request_location=True)]
     ]

main = ReplyKeyboardMarkup(keyboard=main_kb,
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт ниже')

socials_kb = [
    [InlineKeyboardButton(text='vk', url='https://vk.com/im/')],
    [InlineKeyboardButton(text='Youtube', url ='https://www.youtube.com/')]

]

socials = InlineKeyboardMarkup(inline_keyboard=socials_kb)

catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='adidas', callback_data='adidas')],
    [InlineKeyboardButton(text='Nike', callback_data='nike')],
])