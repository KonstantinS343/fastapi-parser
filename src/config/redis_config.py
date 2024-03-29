from pydantic_settings import BaseSettings, SettingsConfigDict


class RedisConfig(BaseSettings):
    host: str
    lamoda_db: int
    twitch_db: int

    model_config = SettingsConfigDict(env_file='../.env', env_file_encoding='utf-8', env_prefix='REDIS_')


redis_settings = RedisConfig()
