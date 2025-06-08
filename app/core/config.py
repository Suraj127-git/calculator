from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_URL: str
    LMSTUDIO_URL: str
    LMSTUDIO_LLM_NAME: str

    class Config:
        env_file = ".env"

settings = Settings()
