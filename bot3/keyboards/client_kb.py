from aiogram.types import ReplyKeyboardMarkup, KeyboardButton#, ReplyKeyboardRemove

b1 = KeyboardButton('/Помощь')
b2 = KeyboardButton('/Функции')
b3 = KeyboardButton('/Дополнительно')



kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).row(b2, b3)




