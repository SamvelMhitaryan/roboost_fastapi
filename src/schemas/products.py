from src.schemas.base import Base
from datetime import datetime
from enum import Enum


class IngredientSchem(Base):
    """Состав."""

    id: int
    name: str


class SupplementSchem(Base):
    """Добавка."""

    id: int
    title: str
    price: int
    category: Enum


class ProductSchem(Base):
    """Продукт."""

    title: str
    image: str
    price: int
    weight: float
    ingredients: list[IngredientSchem]
    supplements: list[SupplementSchem]


class PerPortionSchem(Base):
    """ккал + БЖУ."""

    id: int
    kcal: float
    protein: float
    fat: float
    carbohydrates: float


class OrderSchem(Base):
    """Заказ."""
    id: int
    product_quantity: int
    customer_id: int
    status: Enum
    created_at: datetime
    updated_at: datetime
    supplements: list[SupplementSchem]
    supplement_price: int
    products: list[ProductSchem]


class CreateOrder(Base):
    product_id: int
    product_quantity: int
    supplement_ids: list[int]
