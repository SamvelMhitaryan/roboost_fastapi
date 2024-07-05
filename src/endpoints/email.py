from fastapi_mail import FastMail, MessageSchema
from fastapi import APIRouter, BackgroundTasks


from src.schemas.email import EmailSchem
from src.email.config import conf

email_router = APIRouter(prefix="/email", tags=["email"])


def send_email_background(background_tasks: BackgroundTasks, email_body: EmailSchem):
    message = MessageSchema(
        recipients=email_body.recipients,
        title=email_body.title,
        text=email_body.text,
        subtype="html"
    )
    fm = FastMail(conf)
    background_tasks.add_task(fm.send_message, message)


@email_router.post("/")
async def send_email(background_tasks: BackgroundTasks, email_body: EmailSchem):
    send_email_background(background_tasks, email_body)
    return {"message": f"Email успешно отправлен"}
