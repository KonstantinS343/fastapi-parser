from pydantic_settings import BaseSettings

from .fastapi_config import FastApiConfig, fastapi_settings
from .db_config import MongoDBConfig, mongo_settings
from .redis_config import RedisConfig, redis_settings
from .twitch_config import TwitchConfig, twitch_settings
from .kafka_config import KafkaConfig, kafka_settings


class Settings(BaseSettings):
    fastapi_settings: FastApiConfig = fastapi_settings
    mongo_settings: MongoDBConfig = mongo_settings
    redis_settings: RedisConfig = redis_settings
    twitch_settings: TwitchConfig = twitch_settings
    kafka_settings: KafkaConfig = kafka_settings


settings = Settings()
