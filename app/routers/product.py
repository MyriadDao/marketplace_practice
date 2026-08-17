from fastapi import APIRouter, Depends
from app.schemas import ProductResponse
from app.services import get_all_products, get_product_category, get_product_by_id
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import get_db

#==============================================================================================


router = APIRouter(
    prefix='/products')

#==============================================================================================

@router.get('/', response_model=list[ProductResponse],
summary="Получение всего товара", tags=["Products"])
async def get_products(db: AsyncSession = Depends(get_db)):
    return await get_all_products(db=db)

#==============================================================================================

@router.get('/get_product_by_category/{product_category}', response_model=list[ProductResponse],
summary="Получение товара по категории", tags=["Products"])
async def get_product_by_category(product_category: str, db: AsyncSession = Depends(get_db)):
    return await get_product_category(product_category=product_category, db=db)


@router.get('/get_product_by_id/{product_id}', response_model=ProductResponse,
summary="Получение товара по его id", tags=["Products"])
async def get_product_for_id(product_id: int, db: AsyncSession = Depends(get_db)):
    return await get_product_by_id(product_id=product_id, db=db)
