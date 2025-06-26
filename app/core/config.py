from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_URL: str
    LMSTUDIO_URL: str
    OLLAMA_MODEL: str

    class Config:
        env_file = ".env"

settings = Settings()
