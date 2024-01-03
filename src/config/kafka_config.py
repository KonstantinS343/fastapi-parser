from pydantic_settings import BaseSettings, SettingsConfigDict


class KafkaConfig(BaseSettings):
    bootstrap_servers: str

    model_config = SettingsConfigDict(env_file='../.env', env_file_encoding='utf-8', env_prefix='FASTAPI_')


kafka_settings = KafkaConfig()
