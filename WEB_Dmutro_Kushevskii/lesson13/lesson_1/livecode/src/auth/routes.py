import fastapi
import fastapi.security
import fastapi_mail
import pydantic
import pathlib
import pickle
import redis

import database

import auth.exceptions
import auth.service
import auth.models
import auth.schemas

r = redis.Redis(host="localhost", port=6379, password=None)

auth_service = auth.service.Auth()
router = fastapi.APIRouter(prefix='/auth', tags=["auth"])
mail_conf = fastapi_mail.ConnectionConfig(
    MAIL_USERNAME="fatsapiuser@meta.ua",
    MAIL_PASSWORD="pythonCourse2023",
    MAIL_FROM="fatsapiuser@meta.ua",
    MAIL_PORT=465,
    MAIL_SERVER="smtp.meta.ua",
    MAIL_FROM_NAME="PlanesApi",
    MAIL_STARTTLS=False,
    MAIL_SSL_TLS=True,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True,
    TEMPLATE_FOLDER=pathlib.Path(__file__).parent / 'templates',
)

async def send_email(username, token):
    message = fastapi_mail.MessageSchema(
        subject="Confirm your email ",
        recipients=[username],
        template_body={
            "host": "localhost:8000",
            "username": username,
            "token": token
        },
        subtype=fastapi_mail.MessageType.html
    )

    fm = fastapi_mail.FastMail(mail_conf)
    await fm.send_message(
        message,
        template_name="email_template.html"
    )


@router.post(
    "/signup",
    status_code=fastapi.status.HTTP_201_CREATED
)
async def signup(
    body: auth.schemas.User,
    background_tasks: fastapi.BackgroundTasks,
    db = fastapi.Depends(database.get_database),
) -> auth.schemas.UserDb:
    user = r.get(body.username)
    if not user:
        print("Read from db")
        user = db.query(auth.models.User).filter(
            auth.models.User.username==body.username
        ).first()
    else:
        print("Taken from cache")

    if user is not None:
        raise fastapi.HTTPException(
            fastapi.status.HTTP_409_CONFLICT,
            detail="Account already exists"
        )

    hashed_password = auth_service.hash_password(body.password)

    new_user = auth.models.User(
        username=body.username,
        hash_password=hashed_password
    )

    db.add(new_user)
    db.commit()

    r.set(body.username, pickle.dumps(new_user))

    try:
        token_verification = await auth_service.create_email_token(
            {"sub": body.username}
        )

        background_tasks.add_task(send_email, body.username, token_verification)

    except fastapi_mail.errors.ConnectionErrors as err:
        print(err)

    return new_user


@router.post("/login")
async def login(
    body: fastapi.security.OAuth2PasswordRequestForm = fastapi.Depends(),
    db = fastapi.Depends(database.get_database)
) -> auth.schemas.Token:
    user = db.query(auth.models.User).filter(auth.models.User.username==body.username).first()
    if user is None:
        raise auth.exceptions.AuthException("no such user")

    if (user.confirmed == False):
        raise auth.exceptions.AuthException("not verified")

    verification = auth_service.verify_password(body.password, user.hash_password)
    if not verification:
        raise auth.exceptions.AuthException("incorrect credentials")

    refresh_token = await auth_service.create_refresh_token(payload={"sub": body.username})
    access_token = await auth_service.create_access_token(payload={"sub": body.username})

    user.refresh_token = refresh_token
    db.commit()

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "Bearer"
    }


@router.post("/logout")
async def logout(
    user = fastapi.Depends(auth_service.get_user),
    db = fastapi.Depends(database.get_database)
) -> auth.schemas.LogoutResponse:
    user.refresh_token = None
    db.commit()

    return {"result": "Success"}


@router.get('/confirmed_email/{token}')
async def confirmed_email(
    token: str,
    db = fastapi.Depends(database.get_database)
):
    email = await auth_service.get_email_from_token(token)

    user = db.query(auth.models.User).filter(auth.models.User.username==email).first()
    if user is None:
        raise fastapi.HTTPException(
            status_code=fastapi.status.HTTP_400_BAD_REQUEST,
            detail="Verification error"
        )

    if user.confirmed:
        return {"message": "Your email is already confirmed"}

    user.confirmed = True
    db.commit()

    return {"message": "Email confirmed"}
