from .connect_dp import connect
from .models import Users


async def creart_user(user_data: dict) -> None:
    user = Users.objects(user_id=user_data.get("user_id")).first()
    if user:
        user.first_name = user_data.get("first_name")
        user.last_name = user_data.get("last_name")
        user.language_code = user_data.get("language_code")
        user.is_active = True
    else:
        user: Users = Users(user_data=user_data.get("user_id"),
                             first_name=user_data.get("first_name"),
                             last_name=user_data.get("last_name"),
                             username=user_data.get("username"),
                             language_code=user_data.get("language_code"),)

    user.save()