from pydantic_settings import BaseSettings, SettingsConfigDict


class MongoDBConfig(BaseSettings):
    host: str
    port: int
    db: str

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', env_prefix='MONGO_')


mongo_settings = MongoDBConfig()
