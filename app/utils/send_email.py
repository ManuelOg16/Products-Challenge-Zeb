from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from decouple import config as env_config
from app.config import settings

class Envs:
    MAIL_USERNAME = env_config('MAIL_USERNAME')
    MAIL_PASSWORD = env_config('MAIL_PASSWORD')
    MAIL_FROM = env_config('MAIL_FROM')
    MAIL_PORT = env_config('MAIL_PORT')
    MAIL_SERVER = env_config('MAIL_SERVER')
    MAIL_FROM_NAME = env_config('MAIN_FROM_NAME')


conf = ConnectionConfig(
    MAIL_USERNAME= Envs.MAIL_USERNAME,
    MAIL_PASSWORD=Envs.MAIL_PASSWORD,
    MAIL_FROM= Envs.MAIL_FROM,
    MAIL_PORT=Envs.MAIL_PORT, 
    MAIL_SERVER=Envs.MAIL_SERVER,
    MAIL_FROM_NAME=Envs.MAIL_FROM_NAME,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True,
    MAIL_SSL_TLS=False,
    MAIL_STARTTLS =True
)



async def send_email_async(subject, email,body):
    message = MessageSchema(
        subject=subject,
        recipients=email,
        body=body,
        subtype=MessageType.html,
    )
    
    fm = FastMail(conf)
    await fm.send_message(message)

        