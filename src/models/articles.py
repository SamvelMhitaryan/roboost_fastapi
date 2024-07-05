from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Enum, ForeignKey
from datetime import date
import enum

from src.models.base import Base


class ArticleCategoryEnum(enum.Enum):
    coffee_culture = 'Культура кофе'
    coffee_recipes = 'Рецепты кофе'
    coffee_history = 'История кофе'
    tea_culture = 'Чай и культура'
    recipes = 'Рецепты'


class Article(Base):
    __tablename__ = "articles"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(70))
    cover_image: Mapped[str]
    date: Mapped[date]
    text: Mapped[str]
    image: Mapped[str]
    views: Mapped[int]
    category: Mapped[ArticleCategoryEnum] = mapped_column(
        Enum(ArticleCategoryEnum, native_enum=False, length=50))
    comments: Mapped[list['Comment']] = relationship(
        uselist=True, back_populates='article')
    author: Mapped[str] = mapped_column(nullable=False)

    @property
    def comments_count(self):
        return len(self.comments)

    def __str__(self):
        return self.title


class Comment(Base):
    __tablename__ = "comments"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(80))
    email: Mapped[str] = mapped_column(String(150))
    text: Mapped[str] = mapped_column(String(500))
    web_site: Mapped[str] = mapped_column(nullable=True)
    article_id: Mapped[int] = mapped_column(
        ForeignKey(Article.id, ondelete='CASCADE'))
    article: Mapped[Article] = relationship(back_populates="comments")

    def __str__(self):
        return self.name
