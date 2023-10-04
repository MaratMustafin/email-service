from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Settings
    """

    BACKEND_CORS_ORIGINS: list[AnyHttpUrl] = ["http://localhost"] 
    EMAIL_HOST: str = 'sandbox.smtp.mailtrap.io'
    EMAIL_HOST_USER: str = ''
    EMAIL_HOST_PASSWORD: str = ''
    EMAIL_PORT: int = 2525

settings = Settings()