from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.queries.articles import get_article_and_count_views, create_comment, get_articles_paginated
from src.schemas.articles import ArticleSchem, CommentSchem, PaginateArticleSchem
from src.database import get_db
from annotated_types import Gt, Lt

article_router = APIRouter(prefix="/articles", tags=["articles"])


@article_router.get('/{article_id}/', response_model=ArticleSchem, status_code=status.HTTP_200_OK)
async def get_article(article_id: int, db: AsyncSession = Depends(get_db)):
    """Метод получения статьи"""
    article = await get_article_and_count_views(db, article_id)
    if not article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Article not found")
    return article


@article_router.post('/{article_id}/comments/', response_model=CommentSchem, status_code=status.HTTP_201_CREATED)
async def post_comment(article_id: int, name: str, email: str, text: str, web_site: str, db: AsyncSession = Depends(get_db)):
    """Метод размещения комментария"""
    article = await get_article_and_count_views(article_id=article_id, db=db)
    if not article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Article not found")
    comment = await create_comment(db=db, article_id=article_id, name=name,
                                   email=email, text=text, web_site=web_site)
    return comment


@article_router.get('/list', response_model=PaginateArticleSchem, status_code=status.HTTP_200_OK)
async def article_list(page: Annotated[int, Gt(0)], page_size: Annotated[int, Gt(0), Lt(10)] = 6, db: AsyncSession = Depends(get_db)):
    result = await get_articles_paginated(page=page, page_size=page_size, db=db)
    return result
