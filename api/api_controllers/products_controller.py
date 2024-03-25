from typing import Optional, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from data_base import Products, get_session
from model import ProductIn, ProductOut
from services import ProductsService

router = APIRouter(prefix="/products", tags=["products"])


@router.get("/{product_name}", response_model=Optional[ProductOut])
async def get_product_by_name(product_name: str, session: AsyncSession = Depends(get_session)):
    product = await ProductsService.get_product_by_name(product_name, session)
    if product:
        dto_product = ProductOut(**product.to_dict())
        print()
        return dto_product
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Такого продукта не существует")


@router.get("/", response_model=List[ProductOut])
async def get_all_products(session: AsyncSession = Depends(get_session)):
    products = await ProductsService.get_all_products(session)
    return list(map(lambda x: Products(**x.to_dict()), products))


@router.post("/", response_model=ProductOut)
async def create_product(product_dto: ProductIn, session: AsyncSession = Depends(get_session)):
    # Проверяем существование продукта с таким id или именем

    existing_product_by_name = await ProductsService.get_products_by_name(product_dto.product_name, session)

    if existing_product_by_name:
        raise HTTPException(status_code=400, detail="Product with the same name already exists")

    # Создаем продукт
    product = await ProductsService.create_product(product_dto, session)
    return ProductOut(**product.to_dict())


@router.put("/", response_model=ProductOut)
async def update_product(product_dto: ProductOut, session: AsyncSession = Depends(get_session)):
    product = await ProductsService.get_product_by_id(product_dto.product_id, session)
    if product:
        product.update(product_dto.model_dump())
        await session.commit()
        return ProductOut(**product.to_dict())
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Продукта с таким id не существует")


@router.delete("/")
async def delete_product(product_name: str, session: AsyncSession = Depends(get_session)):
    existing_product_by_name = await ProductsService.get_product_by_name(product_name, session)

    if not existing_product_by_name:
        raise HTTPException(status_code=400, detail=" Not Product with the same name")
    product = await ProductsService.get_product_by_name(product_name, session)
    if product:
        await session.delete(product)
        await session.commit()
        return "status OK"
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Продукта с таким названием не существует")

#TODO: возможность изменять и создавать продукт только для админа(замочек сделать)

