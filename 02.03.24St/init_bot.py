from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from dotenv import dotenv_values

config = dotenv_values(".env")

TOKEN = config.get("TOKEN")

bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()
