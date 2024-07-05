from src.models.questionnaire import StudyEnum
from src.schemas.base import Base
from datetime import date


class QuestionnaireSchem(Base):
    """Анкета."""

    name: str
    surname: str
    phone: str
    accounts: str | None = None
    bithday_date: date
    alcohol: bool
    smoking: bool
    smoking_hqd: bool
    current_employment: bool
    address: str | None = None
    study: StudyEnum | None = None
    last_jobs: str | None = None
    achievements: str | None = None
    why_with_us: str | None = None
