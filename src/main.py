from fastapi import FastAPI

from routers.lamoda import router as lamoda_router
from routers.twitch import router as twitch_router
from config import settings


app = FastAPI()

app.include_router(lamoda_router)
app.include_router(twitch_router)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app=app, host=settings.fastapi_settings.host, port=settings.fastapi_settings.port)
