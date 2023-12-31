from pydantic_settings import BaseSettings, SettingsConfigDict


class FastApiConfig(BaseSettings):
    host: str
    port: int

    model_config = SettingsConfigDict(env_file='../.env', env_file_encoding='utf-8', env_prefix='FASTAPI_')


fastapi_settings = FastApiConfig()
