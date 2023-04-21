from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db

# приветствие
#@dp.message_handler(commands=['start','help'])
async def commands_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id,'Добро пожаловать в Сообщество!',
                               reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Поговорим в личных сообщениях...\n'
                            ' https://t.me/marisatwobot\n'
                            'Добавляйся!')

#@dp.message_handler(commands=['Помощь'])
async def bot_help_info(message : types.Message):
    await bot.send_message(message.from_user.id,'Меня зовут Марисса. Мое предназначение - следить за'
                                                ' чатом группы Сообщества. Я смогу вам помочь всеми'
                                                ' доступными для меня способами. Я вся во внимании!')

#@dp.message_handler(commands=['Функции'])
async def bot_func(message : types.Message):
    await bot.send_message(message.from_user.id,'У меня большой функционал, не бойтесь - все можно '
                                                'пощупать))') #reply_markup=ReplyKeyboardRemove())


dp.message_handler(commands=['Дополнительно'])
async def dop_func_command(message: types.Message):
    await sqlite_db.sql_read(message)

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(bot_help_info, commands=['Помощь'])
    dp.register_message_handler(bot_func, commands=['Функции'])
    dp.register_message_handler(dop_func_command, commands= ['Дополнительно'])
