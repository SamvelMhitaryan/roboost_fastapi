from src.schemas.base import Base
from datetime import date
from enum import Enum


class ArticleSchem(Base):
    """Статья."""

    id: int
    title: str
    cover_image: str
    date: date
    text: str
    image: str
    views: int
    category: Enum
    comments_count: int
    author: str


class PaginateArticleSchem(Base):
    """Пагинация статей."""
    total_articles: int
    total_pages: int
    current_page: int
    page_size: int
    articles: list[ArticleSchem]


class CommentSchem(Base):
    """Комментарий."""

    id: int
    name: str
    email: str
    web_site: str
