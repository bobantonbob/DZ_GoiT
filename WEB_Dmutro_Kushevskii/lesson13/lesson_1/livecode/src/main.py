import fastapi
import uvicorn
import starlette.middleware.base

import auth.routes
import auth.exceptions

import planes.routes
import planes.exceptions

import middlewares

app = fastapi.FastAPI()

app.include_router(planes.routes.router, prefix='/api')
app.include_router(auth.routes.router)

app.add_middleware(
    starlette.middleware.base.BaseHTTPMiddleware,
    dispatch=middlewares.printer_middleware
)

app.add_exception_handler(
    fastapi.HTTPException, 
    planes.exceptions.item_not_found_error_handler
)

app.add_exception_handler(
    auth.exceptions.AuthException,
    auth.exceptions.auth_error_handler
)

if __name__ == "__main__":
    uvicorn.run(
        "main:app", host="localhost", port=8000, reload=True
    )
