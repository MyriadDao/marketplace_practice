from fastapi import HTTPException

from sqlalchemy.orm import Session
from sqlalchemy import select
from app.db.models import Product, Category

#==============================================================================================

def get_all_products(db: Session):
    return db.query(Product).all()

#==============================================================================================

def get_product_category(product_category: str, db: Session):
    query = (
        select(Product)
        .join(Product.category_rel)  # Navigates the relationship key
        .where(Category.name == product_category.capitalize())
    )
    result = db.execute(query)

    if not result:
        raise HTTPException(status_code=404, detail="Товар с такой категорией не найдены!")

    return result.scalars().all()

def get_product_by_id(product_id: int, db: Session):
    query = select(Product).where(Product.id == product_id)
    result = db.execute(query)
    product = result.scalar_one_or_none()

    if not product:
        raise HTTPException(status_code=404, detail="Товар с таким id не найден!")

    return product