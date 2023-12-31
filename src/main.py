from fastapi import FastAPI

from routers.lamoda import router
from config import settings


app = FastAPI()

app.include_router(router)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app=app, host=settings.fastapi_settings.host, port=settings.fastapi_settings.port)
