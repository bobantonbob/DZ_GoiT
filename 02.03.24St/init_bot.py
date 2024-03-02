from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from dotenv import dotenv_values

config = dotenv_values(".env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}

TOKEN = config.get('TOKEN')

bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()