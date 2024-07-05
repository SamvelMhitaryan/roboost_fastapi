from src.schemas.base import Base
import re


def phone_validator(phone: str) -> str:
    """Валидатор номера телефона"""
    if not re.match(r'^\+?1?\d{9,15}$', phone):
        raise ValueError("Invalid phone number format")
    return phone


def password_validator(password: str) -> str:
    """Валидатор пароля"""
    if not re.match(r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*\W)', password):
        raise ValueError('Invalid password format')
    return password


def passwords_match(cls, v, values, **kwargs):
    """Проверка подтверждения пароля"""
    if 'password' in values and v != values['password']:
        raise ValueError('password and confirm_password do not match')
    return v


class UserSchem(Base):
    """Создание пользователя."""
    name: str
    surname: str
    email: str
    phone: str
    password: str


class UserResponseSchem(Base):
    """Получение пользователя."""
    name: str
    surname: str
    email: str
    phone: str


class TokenSchem(Base):
    access_token: str
    token_type: str


class TokenDataSchem(Base):
    username: str | None = None


class UserInDBSchem(Base):
    """Хэширование пароля."""
    hashed_password: str


class UserLoginSchem(Base):
    """Авторизация пользователя."""
    email: str
    password: str
