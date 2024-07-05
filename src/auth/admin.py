from sqladmin.authentication import AuthenticationBackend
from fastapi.responses import RedirectResponse
from fastapi.requests import Request
from datetime import timedelta
from sqlalchemy import select

from src.queries.admin import decode_admin_session_token
from src.settings import ACCESS_TOKEN_EXPIRE_MINUTES
from src.queries.user import create_access_token
from src.auth.utils import verify_password
from src.database import SessionLocal
from src.models.users import User


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        email, password = form["username"], form["password"]
        async with SessionLocal() as session:
            stmt = select(User).where(
                User.email == email).where(User.is_admin.is_(True))
            user = await session.scalar(stmt)
            if user is None:
                return False
        if not verify_password(password=password, hashed_password=user.password):
            return False
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        token = create_access_token(
            data={"email": user.email}, expires_delta=access_token_expires)
        request.session.update({"token": token})
        return True

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        token: str = request.session.get('token')
        if not token:
            return False
        user_email = decode_admin_session_token(token, request)
        if not user_email:
            return RedirectResponse(
                request.url_for("admin:login"), status_code=302,)
        stmt = select(User).where(User.email == user_email)
        async with SessionLocal() as session:
            user = await session.scalar(stmt)
        if user.is_admin is True:
            return True
        return False
