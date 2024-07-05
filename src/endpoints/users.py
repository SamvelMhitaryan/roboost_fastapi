from fastapi import Depends, APIRouter
from typing import Annotated

from src.queries.user import get_current_user
from src.schemas.users import UserSchem
from src.models.users import User

user_router = APIRouter(prefix="/users", tags=["users"])


@user_router.get("/me/", response_model=UserSchem)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_user)]
):
    """Возвращает данные о текущем аутентифицированном пользователе."""
    return current_user


@user_router.get("/me/items/")
async def read_own_items(
    current_user: Annotated[UserSchem, Depends(get_current_user)]
):
    """Пример маршрута, который требует аутентификации и 
    возвращает данные, специфичные для пользователя."""
    return [{"item_id": "Foo", "owner": current_user.email}]
