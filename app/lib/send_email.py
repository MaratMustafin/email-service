from smtplib import SMTP
from app.core.config import settings
from app.core.logger import logger
from ssl import create_default_context
from email.mime.text import MIMEText
from app.usecases.emails.data import EmailOutputData


def send_mail(data: EmailOutputData | None = None) -> dict:
    """
    send_mail
    """
    ctx = create_default_context()
    message = MIMEText(data.message, "html")
    message["From"] = 'player@gmail.com'
    message["To"] = data.to
    message["Subject"] = data.subject

    try:
        with SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT) as server:
            server.starttls(context=ctx)
            server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
            server.send_message(message)
            logger.info(f"Email sended:{message}")
        return 'ok'
    except Exception as e:
        logger.error(f"Email corrupted:{e}")
        return 'bad'