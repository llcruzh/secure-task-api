from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Secure Task API"
    SECRET_KEY: str = "change-me-in-.env"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    ALGORITHM: str = "HS256"
    DATABASE_URL: str = "sqlite:///./secure_tasks.db"

    class Config:
        env_file = ".env"

settings = Settings()
