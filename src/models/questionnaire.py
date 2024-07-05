from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Enum, String, event
from datetime import date
import enum
import re

from src.models.base import Base


class StudyEnum(enum.Enum):
    YES = 'Да, очно'
    YES_BUT = 'Да, заочно'
    NO = 'Нет'


class Questionnaire(Base):
    __tablename__ = "questionnaires"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(70))
    surname: Mapped[str]
    phone: Mapped[str] = mapped_column(unique=True)
    accounts: Mapped[str] = mapped_column(nullable=True)
    bithday_date: Mapped[date]
    alcohol: Mapped[bool]
    smoking: Mapped[bool]
    smoking_hqd: Mapped[bool]
    current_employment: Mapped[bool]
    address: Mapped[str] = mapped_column(nullable=True)
    study: Mapped[StudyEnum] = mapped_column(
        Enum(StudyEnum, native_enum=False, length=50))
    last_jobs: Mapped[str] = mapped_column(String(500), nullable=True)
    achievements: Mapped[str] = mapped_column(String(500), nullable=True)
    why_with_us: Mapped[str] = mapped_column(String(500), nullable=True)

    def __str__(self):
        return f'{self.name} {self.surname}'


def phone_validator(target, value, oldvalue, initiator):
    """Валидатор номера телефона"""
    if not re.match(r'^\+?1?\d{9,15}$', value):
        raise ValueError("Invalid phone number format")
    return value


event.listen(Questionnaire.phone, 'set', phone_validator, retval=True)
