import asyncio
import logging
import sys
import asyncio
import aioschedule

from aiogram import types

from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from src.utils.parser import run_parser
from init_bot import dp, bot
from src.database.crud import create_or_update_user
from src.keyboards.kb import get_main_panel, get_inline_panel
from notification_users import rate_notification


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    data = {"user_id": message.from_user.id, "first_name": message.from_user.first_name,
            "last_name": message.from_user.last_name, "username": message.from_user.username,
            "language_code": message.from_user.language_code}
    panel = await get_main_panel()
    await create_or_update_user(user_data=data)
    await message.answer(text=f"Hello, {hbold(message.from_user.full_name)}!",
                         reply_markup=panel)


@dp.message(Command(commands=["exchange"]))
async def exchange_handler(message: types.Message) -> None:
    """Хендлер який оброблює натискання на кнопку /exchange"""
    print(f"Start /exchange")
    rate_info = await run_parser()
    panel = await get_inline_panel()
    await message.answer(text=rate_info, reply_markup=panel)


@dp.message()
async def echo_handler(message: types.Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")


async def scheduler():
    # for i in ["06:00", "07:00", "08:00", "09:00", "10:00", "11:00", "12:00",
    #           "13:00", "14:00"]:  # 6 годин по UTC - це 9 година по Киеву
    #     aioschedule.every().monday.at(i).do(run_parser)
    #     aioschedule.every().tuesday.at(i).do(run_parser)
    #     aioschedule.every().wednesday.at(i).do(run_parser)
    #     aioschedule.every().thursday.at(i).do(run_parser)
    #     aioschedule.every().friday.at(i).do(run_parser)
    # aioschedule.every().day.at("12:00").do(run_parser)  # кожен день в конкретний час
    # aioschedule.every(2).minutes.do(rate_notification)  # кожен день в конкретний час
    # aioschedule.every().minute.do(rate_notification)  # кожен день в конкретний час
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    # And the run events dispatching
    asyncio.create_task(scheduler())
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
    # asyncio.run(rate_notification())
