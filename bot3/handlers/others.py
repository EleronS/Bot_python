from aiogram import types, Dispatcher
from create_bot import dp
import json, string

#@dp.message_handler()
async def cenz_filtr(message: types.Message):
    if{i.lower().translate(str.maketrans('','',string.punctuation))for i in message.text.split(' ')}\
    .intersection(set(json.load(open('cenz_list.json')))) != set():
        await message.reply("Не стоит так!")
        await message.delete()

def register_handlers_others(dp : Dispatcher):
    dp.register_message_handler(cenz_filtr)