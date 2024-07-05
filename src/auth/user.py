from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import timedelta

from src.schemas.users import TokenSchem, UserLoginSchem, UserSchem, UserResponseSchem
from src.queries.user import create_access_token, create_user_query
from src.settings import ACCESS_TOKEN_EXPIRE_MINUTES
from src.auth.utils import authenticate_user
from src.database import get_db


auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.post('/registration', response_model=UserResponseSchem)
async def create_user(user_schem: UserSchem, db: AsyncSession = Depends(get_db)):
    user = await create_user_query(user_schem, db)
    if not user:
        raise Exception('no user for create')
    return user


@auth_router.post("/login")
async def login_for_access_token(
    form_data: UserLoginSchem,
    db: AsyncSession = Depends(get_db)
) -> TokenSchem:
    """Вход в систему для получения токена."""
    user = await authenticate_user(
        db, form_data.email, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"email": user.email}, expires_delta=access_token_expires)
    return TokenSchem(access_token=access_token, token_type="Bearer")
