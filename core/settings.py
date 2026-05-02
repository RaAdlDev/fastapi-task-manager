from pydantic_settings import SettingsConfigDict, BaseSettings

class Settings(BaseSettings):
    secret_key: str
    debug: bool = False

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()