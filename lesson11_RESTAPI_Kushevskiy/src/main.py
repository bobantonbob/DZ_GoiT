import uvicorn
import fastapi

import contacts.routers

contact_api = fastapi.FastAPI()
contact_api.include_router(contacts.routers.router)





if __name__ == "__main__":
    uvicorn.run("main:contact_api", host="0.0.0.0", port=8000, reload=True)
