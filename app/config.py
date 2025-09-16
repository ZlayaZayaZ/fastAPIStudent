# import os
# from pydantic_settings import BaseSettings, SettingsConfigDict
#
#
# class Settings(BaseSettings):
#     DB_HOST: str
#     DB_PORT: int
#     DB_NAME: str
#     DB_USER: str
#     DB_PASSWORD: str
#     model_config = SettingsConfigDict(
#         env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "", ".env")
#     )
#
#
# settings = Settings()
#
#
# def get_db_url():
#     return (f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASSWORD}@"
#             f"{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}")

from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    DB_HOST: str = Field(..., env="DB_HOST")
    DB_PORT: int = Field(..., env="DB_PORT")
    DB_NAME: str = Field(..., env="DB_NAME")
    DB_USER: str = Field(..., env="DB_USER")
    DB_PASSWORD: str = Field(..., env="DB_PASSWORD")

    class Config:
        env_file = ".env"
        extra = "ignore"

    @property
    def DATABASE_URL(self):
        return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


settings = Settings()


def get_db_url():
    return (f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASSWORD}@"
            f"{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}")