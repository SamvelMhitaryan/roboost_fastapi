from fastapi_mail import ConnectionConfig


class EmailConfig:
    MAIL_USERNAME = "test_email@example.com"
    MAIL_PASSWORD = "test_password"
    MAIL_FROM = "test_email@example.com"
    MAIL_PORT = 587  # Порт SMTP
    MAIL_SERVER = "smtp.test.com"  # Сервер SMTP
    MAIL_STARTTLS = True
    MAIL_SSL_TLS = False
    USE_CREDENTIALS = True
    VALIDATE_CERTS = True


conf = ConnectionConfig(
    MAIL_USERNAME=EmailConfig.MAIL_USERNAME,
    MAIL_PASSWORD=EmailConfig.MAIL_PASSWORD,
    MAIL_FROM=EmailConfig.MAIL_FROM,
    MAIL_PORT=EmailConfig.MAIL_PORT,
    MAIL_SERVER=EmailConfig.MAIL_SERVER,
    MAIL_STARTTLS=EmailConfig.MAIL_STARTTLS,
    MAIL_SSL_TLS=EmailConfig.MAIL_SSL_TLS,
    USE_CREDENTIALS=EmailConfig.USE_CREDENTIALS,
    VALIDATE_CERTS=EmailConfig.VALIDATE_CERTS
)
