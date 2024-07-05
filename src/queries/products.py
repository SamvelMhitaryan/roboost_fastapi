from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from sqlalchemy import select

from src.models.products import Product, Ingredient, Order, Supplement, OrderProduct, OrderSupplement


async def get_product_by_id(db: AsyncSession, product_id: int):
    """Метод фильтрации продуктов по id."""
    stmt = select(Product).where(Product.id == product_id).options(
        selectinload(Product.ingredients), selectinload(Product.supplements))
    result = await db.scalars(stmt)
    return result.first()


async def get_all_products(db: AsyncSession) -> list[Product | None]:
    """Метод получения списка всех продуктов."""
    stmt = select(Product).options(selectinload(
        Product.ingredients))
    result = await db.scalars(stmt)
    return result.all()


async def get_ingredient_by_id(db: AsyncSession, ingredient_id: int):
    """Метод фильтрации ингредиентов."""
    stmt = select(Ingredient).where(Ingredient.id == ingredient_id)
    result = await db.scalars(stmt)
    return result.first()


async def check_product_exist(db: AsyncSession, product_id: list[int]):
    """Метод проверки существования списка продуктов."""
    stmt = select(Product).where(Product.id.in_(product_id))
    result = await db.scalars(stmt)
    if not result:
        raise Exception('Product is not found')
    return result


async def calculate_order_total(order_id, db: AsyncSession) -> int:
    """Расчет общей суммы заказа."""
    stmt = select(Order).where(id=order_id)
    order = db.scalar(stmt)
    if not order:
        raise Exception('no order')

    total_sum = 0

    product_associations = select(
        OrderProduct).where(OrderProduct.order_id == order_id)
    product_ids = [
        association.product_id for association in product_associations]
    products = select(Product).where(Product.id.in_(product_ids))
    result = await db.scalars(products)
    for product in result:
        total_sum += product.price * association.quantity

    supplement_associations = select(
        OrderSupplement).where(OrderSupplement.order_id == order_id)
    supplement_ids = [
        association.supplement_id for association in supplement_associations]
    supplement = select(Supplement.where(Supplement.id.in_(supplement_ids)))
    result = await db.scalars(products)
    for association in result:
        if supplement:
            total_sum += supplement.price * association.quantity

    return total_sum
