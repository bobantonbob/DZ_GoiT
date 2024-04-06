import fastapi
import uvicorn
import starlette.middleware.base

import planes.routes
import planes.exceptions

import middlewares

app = fastapi.FastAPI()

app.include_router(planes.routes.router, prefix='/api')

app.add_middleware(
    starlette.middleware.base.BaseHTTPMiddleware,
    dispatch=middlewares.printer_middleware
)

app.add_exception_handler(
    fastapi.HTTPException, 
    planes.exceptions.item_not_found_error_handler
)

if __name__ == "__main__":
    uvicorn.run(
        "main:app", host="localhost", port=8000, reload=True
    )
