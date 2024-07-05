from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.schemas.questionnaire import QuestionnaireSchem
from src.models.questionnaire import Questionnaire
from src.database import get_db


async def questionnaire_create(questionnaire_data: QuestionnaireSchem, db: AsyncSession = Depends(get_db)):
    questionnaire = Questionnaire(**questionnaire_data.model_dump())
    db.add(questionnaire)
    try:
        await db.commit()
    except Exception as e:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error while saving to database: {e}")
    await db.refresh(questionnaire)
    return questionnaire
