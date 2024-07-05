from pydantic import EmailStr

from src.schemas.base import Base


class EmailSchem(Base):
    """Email."""

    recipients: list[EmailStr]
    title: str
    text: str
