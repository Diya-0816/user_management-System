from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from app.core.config import settings
from pydantic import EmailStr

conf = ConnectionConfig(
    MAIL_USERNAME=settings.MAIL_USERNAME,
    MAIL_PASSWORD=settings.MAIL_PASSWORD,
    MAIL_FROM=settings.MAIL_FROM,
    MAIL_PORT=587,
    MAIL_SERVER="smtp.mailtrap.io",
    MAIL_TLS=True,
    MAIL_SSL=False,
    USE_CREDENTIALS=True
)

async def send_verification_email(email: EmailStr, token: str):
    message = MessageSchema(
        subject="Verify Account",
        recipients=[email],
        body=f"Click this link: https://yourapp.com/verify?token={token}",
        subtype="html"
    )
    fm = FastMail(conf)
    await fm.send_message(message)
