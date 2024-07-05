from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from sqlalchemy.orm import selectinload

from src.models.articles import Article, Comment


async def get_comment_by_id(db: AsyncSession, comment_id: int):
    """Метод нахождения нужного коммента."""
    stmt = select(Comment).where(Comment.id == comment_id)
    return await db.scalar(stmt)


async def create_comment(db: AsyncSession, article_id: int, name: str, email: str, text: str, web_site: str):
    """Метод создания комментария."""
    new_comment = Comment(article_id=article_id, name=name,
                          email=email, text=text, web_site=web_site)
    db.add(new_comment)
    await db.commit()
    await db.refresh(new_comment)
    return new_comment


async def get_article_and_count_views(db: AsyncSession, article_id: int):
    stmt = select(Article).where(Article.id == article_id).options(
        selectinload(Article.comments))
    result = await db.execute(stmt)
    article = result.scalars().first()
    if article:
        article.views += 1
        await db.commit()
        return article
    else:
        raise ValueError("Article not found")


async def get_articles_paginated(db: AsyncSession, page: int, page_size: int = 6):
    """Метод для получения списка статей с пагинацией и общим количеством."""
    offset = (page - 1) * page_size
    # Получаем общее количество статей для пагинации
    total_stmt = select(func.count(Article.id))
    total_result = await db.execute(total_stmt)
    total_articles = total_result.scalar()
    # Получаем статьи с учетом пагинации
    stmt = select(Article).options(
        selectinload(Article.comments)).offset(offset).limit(page_size)
    result = await db.execute(stmt)
    articles = result.scalars().all()
    # Рассчитываем общее количество страниц
    total_pages = (total_articles + page_size -
                   1) // page_size  # Округление вверх
    return {
        "total_articles": total_articles,
        "total_pages": total_pages,
        "current_page": page,
        "page_size": page_size,
        "articles": articles
    }
