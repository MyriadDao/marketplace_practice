from fastapi import HTTPException
from sqlalchemy.orm import selectinload

from app.schemas import ProductResponse
from sqlalchemy.orm import Session, joinedload
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete, func
from app.db.models import Product

#==============================================================================================

def get_all_products(db: Session):

    return db.query(Product).all()

#==============================================================================================

async def get_product_category(product_category: str, db: AsyncSession):
    query = select(Product).where(Product.category == product_category.capitalize())
    result = await db.execute(query)
    products = result.scalars().all()
    if not products:
        raise HTTPException(status_code=404, detail="Товар с такой категорией не найдены!")
    return products

async def get_product_by_id(product_id: int, db: AsyncSession):
    query = select(Product).where(Product.id == product_id)
    result = await db.execute(query)
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Товар с таким id не найден!")
    return product