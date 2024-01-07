from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

from bson.errors import InvalidId

from routers.lamoda import router as lamoda_router
from routers.twitch import router as twitch_router
from config import settings


app = FastAPI()

app.include_router(lamoda_router)
app.include_router(twitch_router)


@app.exception_handler(Exception)
async def unicorn_exception_handler(request, exc):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    content = {'message': str(exc)}
    if isinstance(exc, ValueError) or isinstance(exc, InvalidId):
        status_code = status.HTTP_400_BAD_REQUEST
    return JSONResponse(
        status_code=status_code,
        content=content,
    )


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app=app, host=settings.fastapi_settings.host, port=settings.fastapi_settings.port)
