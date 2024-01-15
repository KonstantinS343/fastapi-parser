from pydantic_settings import BaseSettings, SettingsConfigDict


class TwitchConfig(BaseSettings):
    client_id: str
    client_secret: str

    model_config = SettingsConfigDict(env_file='../.env', env_file_encoding='utf-8', env_prefix='TWITCH_')


twitch_settings = TwitchConfig()
