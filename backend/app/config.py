from pydantic import BaseSettings

class Settings(BaseSettings):
    MONGO_URL: str
    APP_NAME: str = "FastAPI Production App"

    class Config:
        env_file = ".env"

settings = Settings()