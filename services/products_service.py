from typing import Optional, List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from data_base import Products
from model.products import ProductIn, ProductOut


class ProductsService:
    @staticmethod
    async def get_products_by_name(product_name: str,
                                   session: AsyncSession) -> Optional[Products]:
        query = await session.execute(select(Products).where(Products.product_name == product_name))
        product = query.scalars().first()
        return product

    @staticmethod
    async def get_product_by_id(product_id: int,
                             session: AsyncSession) -> Optional[Products]:
        query = await session.execute(select(Products).where(Products.product_id == product_id))
        product = query.scalars().first()
        return product

    @staticmethod
    async def get_all_products(session: AsyncSession) -> List[Products]:
        query = await session.execute(select(Products).order_by(Products.product_id))
        products = query.scalars().all()
        return products

    @staticmethod
    async def create_product(product_dto: ProductIn, session: AsyncSession) -> Products:
        product = Products(**product_dto.model_dump())
        session.add(product)
        await session.commit()
        return product


