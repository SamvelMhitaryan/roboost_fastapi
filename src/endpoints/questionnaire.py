from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.queries.questionnaire import questionnaire_create
from src.schemas.questionnaire import QuestionnaireSchem
from src.database import get_db

questionnaire_router = APIRouter(
    prefix="/questionnaire", tags=["questionnaire"])


@questionnaire_router.post('/', response_model=QuestionnaireSchem, status_code=status.HTTP_201_CREATED)
async def questionnaire_form(questionnaire_data: QuestionnaireSchem, db: AsyncSession = Depends(get_db)):
    result = await questionnaire_create(questionnaire_data, db)
    return result
