from src.queries.user import get_user_by_email
from src.settings import pwd_context
from src.models.users import User


def get_password_hash(password) -> str:
    """Хэширует пароль."""
    return pwd_context.hash(password)


def verify_password(password, hashed_password) -> bool:
    """Верифицирует пароль."""
    return pwd_context.verify(password, hashed_password)


async def authenticate_user(db, email: str, password: str) -> User | None:
    """Аутентифицирует пользователя проверяя его пароль."""
    user = await get_user_by_email(db, email)
    if user and verify_password(password, user.password):
        return user
    return None
