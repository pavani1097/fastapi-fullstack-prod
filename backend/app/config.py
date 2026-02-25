from pydantic import BaseSettings

class Settings(BaseSettings):
    MONGO_URL: str
    APP_NAME: str = "FastAPI Production App"

    class Config:
        env_file = Path(__file__).parent.parent / ".env"

settings = Settings()