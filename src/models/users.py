from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    surname: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    phone: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    is_admin: Mapped[bool] = mapped_column(default=False)

    def __str__(self):
        return f'{self.name} {self.surname}'
