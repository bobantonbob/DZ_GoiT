from .connect_db import connect
from .models import Users


async def create_or_update_user(user_data: dict) -> None:
    user = Users.objects(user_id=user_data.get("user_id")).first()
    if user:
        user.first_name = user_data.get("first_name")
        user.last_name = user_data.get("last_name")
        user.language_code = user_data["language_code"]
        user.is_active = True
    else:
        user: Users = Users(user_id=user_data.get("user_id"),
                            first_name=user_data.get("first_name"),
                            last_name=user_data["last_name"],
                            username=user_data["username"],
                            language_code=user_data["language_code"])
    user.save()


async def get_all_users():
    users = Users.objects(is_active=True).all()
    return users
