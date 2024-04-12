from fastapi_cors import CORS
from fastapi import FastAPI

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORS,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/healthcheck")
def read_root():
     return {"status": "ok"}
