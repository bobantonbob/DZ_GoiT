from src.utils.parser import run_parser
from src.database.crud import get_all_users
from init_bot import bot


async def rate_notification():
    rate_info = await run_parser()
    users = await get_all_users()
    if users:
        for user in users:
            await bot.send_message(chat_id=user.user_id, text=rate_info)

