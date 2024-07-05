from fastapi import HTTPException, Request, status
from sqlalchemy.ext.asyncio import AsyncSession
from jose import JWTError, jwt
from typing import Optional

from src.settings import SECRET_KEY, ALGORITHM
from src.queries.user import get_user_by_email
from src.auth.utils import verify_password
from src.models.users import User


async def authenticate_admin(db: AsyncSession, email: str, password: str) -> Optional[User]:
    """Аутентифицирует пользователя, проверяя его пароль и статус администратора."""
    user = await get_user_by_email(db, email)
    if user and verify_password(password, user.hashed_password) and user.is_admin:
        return user
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                        detail="Not authorized or not an admin")


def decode_admin_session_token(token: str, request: Request) -> str | bool:
    try:
        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
        email: str = payload.get("email")
        if email is None:
            raise Exception('Email is None')
    except JWTError:
        return False
    return email
