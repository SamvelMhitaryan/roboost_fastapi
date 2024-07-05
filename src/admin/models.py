from sqladmin import ModelView

from src.models.products import Product, PerPortion, Ingredient, Supplement
from src.models.questionnaire import Questionnaire
from src.models.articles import Article, Comment
from src.models.users import User


class ProductAdmin(ModelView, model=Product):
    column_list = '__all__'
    column_labels = {Product.title: 'Продукт',
                     Product.image: 'Картинка',
                     Product.price: 'Цена',
                     Product.weight: 'Объем',
                     Product.ingredients: 'Ингредиенты'

                     }


class PerPortionAdmin(ModelView, model=PerPortion):
    column_list = '__all__'


class IngredientAdmin(ModelView, model=Ingredient):
    column_list = '__all__'


class SupplementsAdmin(ModelView, model=Supplement):
    column_list = '__all__'


class ArticleAdmin(ModelView, model=Article):
    column_list = '__all__'


class CommentAdmin(ModelView, model=Comment):
    column_list = '__all__'


class UserAdmin(ModelView, model=User):
    column_list = '__all__'


class QuestionnaireAdmin(ModelView, model=Questionnaire):
    column_list = '__all__'
