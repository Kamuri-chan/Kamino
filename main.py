import traceback
import logging
from aiogram import Bot, Dispatcher, executor, types
import datetime
import re
import json
from process_message import ChatterMessage


with open('config.json', 'r') as f:
	config_keys = json.load(f)

API_TOKEN = config_keys['API_KEY']
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def init(message: types.Message):
	response = "Nyahello! Envie alguma mensagem e irei responder!"
	await message.reply(response)


@dp.message_handler()
async def main(message: types.Message):
	not_send = [' ', None]
	response = None
	meta_reponse = ChatterMessage(message['text'])
	response = meta_reponse.response
	if response not in not_send:
		await message.reply(response)


if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)

