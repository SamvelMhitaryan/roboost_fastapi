from fastapi import FastAPI
from sqladmin import Admin
from pathlib import Path
import uvicorn
import sys


sys.path.insert(0, Path(__file__).parent.as_posix())


from src.endpoints.articles import article_router  # noqa
from src.endpoints.products import product_router  # noqa
from src.endpoints.email import email_router  # noqa
from src.database import sync_engine as engine  # noqa
from src.endpoints.questionnaire import questionnaire_router  # noqa
from src.endpoints.users import user_router  # noqa
from src.auth.user import auth_router  # noqa
from src.auth.admin import AdminAuth  # noqa
from src.settings import SECRET_KEY  # noqa
from src.admin.models import (
    ProductAdmin,
    PerPortionAdmin,
    IngredientAdmin,
    ArticleAdmin,
    CommentAdmin,
    SupplementsAdmin,
    UserAdmin,
    QuestionnaireAdmin)  # noqa

app = FastAPI()
admin = Admin(app=app, engine=engine,
              authentication_backend=AdminAuth(SECRET_KEY))

app.include_router(article_router)
app.include_router(product_router)
app.include_router(user_router)
app.include_router(auth_router)
app.include_router(email_router)
app.include_router(questionnaire_router)

admin.add_view(ProductAdmin)
admin.add_view(PerPortionAdmin)
admin.add_view(IngredientAdmin)
admin.add_view(ArticleAdmin)
admin.add_view(CommentAdmin)
admin.add_view(SupplementsAdmin)
admin.add_view(UserAdmin)
admin.add_view(QuestionnaireAdmin)


if __name__ == "__main__":
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)
