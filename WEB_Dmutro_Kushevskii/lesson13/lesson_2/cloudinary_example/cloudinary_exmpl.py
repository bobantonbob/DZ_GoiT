import redis.asyncio as redis

from decouple import config

import uvicorn
import fastapi
from contextlib import asynccontextmanager

from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

import cloudinary
import cloudinary.uploader

r = None

@asynccontextmanager
async def lifespan(app: fastapi.FastAPI):
    global r

    r = await redis.Redis(
        host='localhost', port=6379, db=0,
        encoding="utf-8", decode_responses=True
    )

    yield

    r.close()

app = fastapi.FastAPI(lifespan=lifespan)

limiter = Limiter(key_func=get_remote_address)

app.state.limiter = limiter
app.add_exception_handler(
    RateLimitExceeded, _rate_limit_exceeded_handler
)


@app.get("/")
@limiter.limit("5/minute")
async def index(request: fastapi.Request):
    avatar = await r.get("avatar")
    return  {"avatar": avatar}

@app.post('/avatar')
async def update_avatar_user(
    file: fastapi.UploadFile = fastapi.File()
):
    cloudinary.config(
        cloud_name=config("cloud_name"),
        api_key=config("api_key"),
        api_secret=config("api_secret"),
        secure=True
    )

    req = cloudinary.uploader.upload(file.file, public_id='root', overwrite=True)

    src_url = cloudinary.CloudinaryImage('root').build_url(
        width=250, height=250, crop='fill', version=req.get('version')
    )

    await r.set("avatar", src_url)

    return {"ok": True}


if __name__ == "__main__":
    uvicorn.run("cloudinary_exmpl:app", reload=True)
