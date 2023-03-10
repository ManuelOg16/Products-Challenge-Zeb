import os

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    db_url: str = Field(..., env='DATABASE_URL')
    secrest_jwt: str = Field(..., env='JWT_SECRET')

    class Config:
            env_file = ".env"
settings = Settings()

