from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Enum, String, DateTime
from datetime import datetime
import enum

from src.models.base import Base


class ProductIngredient(Base):
    __tablename__ = 'product_ingredient'

    id: Mapped[int] = mapped_column(primary_key=True)
    product_id: Mapped[int] = mapped_column(
        ForeignKey('products.id', ondelete='CASCADE'))
    ingredient_id: Mapped[int] = mapped_column(
        ForeignKey('ingredients.id', ondelete='CASCADE'))


class ProductSupplements(Base):
    __tablename__ = 'product_supplements'

    id: Mapped[int] = mapped_column(primary_key=True)
    product_id: Mapped[int] = mapped_column(
        ForeignKey('products.id', ondelete='CASCADE'))
    supplements_id: Mapped[int] = mapped_column(
        ForeignKey('supplements.id', ondelete='CASCADE'))


class ProductCategoryEnum(enum.Enum):
    CLASSIC = 'КЛАССИКА'
    BRANDED_BOOST = 'ФИРМЕННЫЕ BOOST'
    OTHER = 'ПРОЧЕЕ'
    BAKERY = 'ВЫПЕЧКА'
    DESSERT = 'ДЕСЕРТЫ'
    NUTRITIONAL = 'СЫТНОЕ'


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(70), unique=True)
    image: Mapped[str]
    price: Mapped[int]
    weight: Mapped[float | None]
    ingredients: Mapped[list['Ingredient']] = relationship(
        "Ingredient", secondary="product_ingredient",
        back_populates="products", uselist=True)
    perportion: Mapped['PerPortion'] = relationship(
        "PerPortion", back_populates="product", uselist=False)
    supplements: Mapped[list['Supplement']] = relationship(
        "Supplement", secondary='product_supplements',
        back_populates="products", uselist=True)
    category: Mapped[ProductCategoryEnum] = mapped_column(
        Enum(ProductCategoryEnum, native_enum=False, length=50))
    orders: Mapped[list['Order']] = relationship(
        "Order", secondary='order_products', back_populates="products", uselist=True)

    def __str__(self):
        return self.title


class Ingredient(Base):
    __tablename__ = "ingredients"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    products: Mapped[list['Product']] = relationship(
        "Product",
        secondary="product_ingredient",
        back_populates="ingredients"
    )

    def __str__(self):
        return self.name


class PerPortion(Base):
    __tablename__ = "perportion"

    id: Mapped[int] = mapped_column(primary_key=True)

    kcal: Mapped[float]
    protein: Mapped[float]
    fat: Mapped[float]
    carbohydrates: Mapped[float]
    product_id: Mapped[int] = mapped_column(ForeignKey('products.id'))
    product: Mapped[Product] = relationship(
        "Product", back_populates="perportion")

    def __str__(self):
        return f'ккал: {self.kcal}, белки: {self.protein}, жиры: {self.fat}, углеводы: {self.carbohydrates}'


class SupplementsCategoryEnum(enum.Enum):
    extras = 'Добавки'
    syrup = 'Сироп'
    milk = 'Молоко'
    fresh = 'Фреш'


class Supplement(Base):
    __tablename__ = "supplements"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(70), unique=True)
    price: Mapped[int]
    category: Mapped[SupplementsCategoryEnum] = mapped_column(
        Enum(SupplementsCategoryEnum, native_enum=False, length=50))
    product_id: Mapped[int] = mapped_column(
        ForeignKey('products.id', ondelete='CASCADE'))
    products: Mapped[Product] = relationship(
        "Product", back_populates="supplements")
    orders: Mapped['Order'] = relationship(
        "Order",
        secondary='order_supplements',
        back_populates="supplements"
    )

    def __str__(self):
        return self.title


class OrderProduct(Base):
    __tablename__ = 'order_products'

    id: Mapped[int] = mapped_column(primary_key=True)
    product_id: Mapped[int] = mapped_column(
        ForeignKey('products.id', ondelete='CASCADE'))
    order_id: Mapped[int] = mapped_column(
        ForeignKey('orders.id', ondelete='CASCADE'))
    supplements: Mapped[int] = mapped_column(
        ForeignKey('supplements.id', ondelete='CASCADE'))
    quantity: Mapped[int] = mapped_column(default=0)


class OrderSupplement(Base):
    __tablename__ = 'order_supplements'

    id: Mapped[int] = mapped_column(primary_key=True)
    supplement_id: Mapped[int] = mapped_column(
        ForeignKey('supplements.id', ondelete='CASCADE'))
    order_id: Mapped[int] = mapped_column(ForeignKey(
        'orders.id', ondelete='CASCADE'))
    quantity: Mapped[int] = mapped_column(default=0)


class OrderEnum(enum.Enum):
    accepted = 'Принято'
    getting_ready = 'Начинаем готовить'
    ready = 'Заказ готов'


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    customer_id: Mapped[int]
    status: Mapped[OrderEnum] = mapped_column(
        Enum(OrderEnum, native_enum=False, length=50))
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now, onupdate=datetime.now)
    supplements: Mapped[list[Supplement]] = relationship(
        "Supplement",
        secondary='order_supplements',
        back_populates="orders")
    products: Mapped[list[Product]] = relationship(
        "Product", secondary='order_products',
        back_populates="orders", uselist=True)

    def __str__(self):
        return self.products
