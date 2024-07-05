from datetime import datetime, timedelta, timezone
from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, select
from jose import JWTError, jwt
from typing import Annotated

from src.settings import SECRET_KEY, ALGORITHM, oauth2_scheme
from src.schemas.users import UserSchem, UserInDBSchem
from src.models.users import User
from src.database import get_db


def get_user(db, email: str):
    """Возвращает пользователя из базы данных."""
    if email in db:
        user_dict = db[email]
        return UserInDBSchem(**user_dict)
    raise Exception('No user in database')


async def get_user_by_email(db: AsyncSession, email: str) -> User:
    """Возвращает пользователя по почте."""
    stmt = select(User).where(User.email == email)
    result = await db.scalars(stmt)
    user = result.first()
    if not user:
        raise Exception('No user with this email')
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    """Создает токен JWT, который истекает через заданное время."""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(
        token: Annotated[str, Depends(oauth2_scheme)],
        db: AsyncSession = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"})
    """извлекает текущего пользователя из токена."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise credentials_exception
    email: str = payload.get("email")
    if email is None:
        raise credentials_exception
    user = await get_user_by_email(db, email=email)
    if user is None:
        raise credentials_exception
    return user

from src.auth.utils import get_password_hash  # noqa


async def create_user_query(user_schem: UserSchem, db: AsyncSession) -> User:
    """Создает пользователя."""
    stmt = insert(User).values(
        name=user_schem.name,
        surname=user_schem.surname,
        email=user_schem.email,
        phone=user_schem.phone,
        password=get_password_hash(user_schem.password)).returning(User)
    user = await db.scalar(stmt)
    if not user:
        raise Exception('User is not created.')
    await db.commit()
    return user
