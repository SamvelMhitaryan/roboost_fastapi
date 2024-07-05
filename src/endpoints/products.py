from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.products import Order
from src.queries.products import get_product_by_id, get_ingredient_by_id, get_all_products
from src.schemas.products import ProductSchem, IngredientSchem, CreateOrder, OrderSchem
from src.database import get_db

product_router = APIRouter(prefix="/products", tags=["products"])


@product_router.get('/{product_id}/', response_model=ProductSchem, status_code=status.HTTP_200_OK)
async def get_product(product_id: int, db: AsyncSession = Depends(get_db)):
    """Метод получения продукта."""
    product = await get_product_by_id(db, product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return product


@product_router.get('/', response_model=list[ProductSchem], status_code=status.HTTP_200_OK)
async def get_list_products(db: AsyncSession = Depends(get_db)):
    """Метод получения списка всех продуктов."""
    return await get_all_products(db)


@product_router.get('/ingredients/{ingredient_id}/', response_model=IngredientSchem, status_code=status.HTTP_200_OK)
async def get_ingredient(ingredient_id: int, db: AsyncSession = Depends(get_db)):
    """Метод получения ингредиентов."""
    ingredient = await get_ingredient_by_id(db, ingredient_id)
    if not ingredient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Ingredient not found")
    return ingredient


@product_router.post('/orders/', response_model=OrderSchem, status_code=status.HTTP_200_OK)
async def make_order(order_data: list[CreateOrder], db: AsyncSession = Depends(get_db)):
    """Метод создания заказа."""
    new_order = Order(
        product_quantity=order_data.product_quantity,
        customer_id=order_data.customer_id,
        status=order_data.status
    )
    db.add(new_order)
    await db.commit()
    await db.refresh(new_order)
    return new_order
