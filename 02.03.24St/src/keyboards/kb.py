from aiogram.types import KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup

from src.utils.parser import NBU_URL


async def get_main_panel():
    buttons = [[KeyboardButton(text="/exchange")], [KeyboardButton(text="/button1"), KeyboardButton(text="/button2")]]
    kb = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    return kb


async def get_inline_panel():
    buttons = [[InlineKeyboardButton(text="Click me", url=NBU_URL),
                InlineKeyboardButton(text="Click me", web_app=WebAppInfo(url="https://rozetka.com.ua/"))]]
    kb = InlineKeyboardMarkup(inline_keyboard=buttons)
    return kb
