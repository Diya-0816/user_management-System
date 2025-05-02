from pydantic import BaseSettings

class Settings(BaseSettings):
    MAIL_USERNAME: str = "your@mail.com"
    MAIL_PASSWORD: str = "password"
    MAIL_FROM: str = "your@mail.com"

settings = Settings()
