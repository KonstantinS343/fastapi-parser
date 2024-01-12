from typing import List
import re
import ast

from models.lamoda import Product
from models.twitch import Twitch, Stream


async def parse_redis_result(redis: str | List[Product | Twitch | Stream]) -> List[Product | Twitch | Stream]:
    if isinstance(redis, list):
        return redis
    pattern = r"\{[^}]*\}"
    matches = re.findall(pattern, redis)
    converted_redis = []
    for i in matches:
        dict_data = ast.literal_eval(i)
        converted_redis.append(dict_data)

    return converted_redis
