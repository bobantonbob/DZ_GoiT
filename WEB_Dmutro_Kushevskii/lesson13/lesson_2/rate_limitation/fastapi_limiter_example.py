import redis.asyncio as redis

import uvicorn
import fastapi
from contextlib import asynccontextmanager

import fastapi.middleware.cors as cors_middleware

from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

r = None
limiter = Limiter(key_func=get_remote_address)

@asynccontextmanager
async def lifespan(app: fastapi.FastAPI):
    global r
    global limiter

    app.state.limiter = limiter
    app.add_exception_handler(
        RateLimitExceeded, _rate_limit_exceeded_handler
    )

    r = await redis.Redis(
        host='localhost', port=6379, db=0,
        encoding="utf-8", decode_responses=True
    )

    yield

    r.close()

app = fastapi.FastAPI(lifespan=lifespan)

origins = [
    "https://kek.com",
    "https://www.google.com",
]

app.add_middleware(
    cors_middleware.CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
@limiter.limit("5/minute")
async def index(request: fastapi.Request):
    return {"msg": "Hello World"}


if __name__ == "__main__":
    uvicorn.run("fastapi_limiter_example:app", reload=True)
