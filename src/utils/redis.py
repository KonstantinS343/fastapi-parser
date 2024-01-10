from redis.asyncio import from_url  # type: ignore

from typing import Any

from config import settings


async def get_cache(key: str, type: str):
    redis = await from_url(
        f'redis://{settings.redis_settings.host}/{settings.redis_settings.lamoda_db if type == "lamoda" else settings.redis_settings.twitch_db}'
    )

    result = await redis.get(key)
    await redis.close()
    return result


async def set_cache(key: str, value: Any, type: str):
    redis = await from_url(
        f'redis://{settings.redis_settings.host}/{settings.redis_settings.lamoda_db if type == "lamoda" else settings.redis_settings.twitch_db}'
    )

    await redis.set(key, str(value))
    await redis.close()


async def clear_cache(key: str, type: str):
    redis = await from_url(
        f'redis://{settings.redis_settings.host}/{settings.redis_settings.lamoda_db if type == "lamoda" else settings.redis_settings.twitch_db}'
    )

    await redis.delete(key)
