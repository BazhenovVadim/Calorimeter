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
        product: Products = query.scalars().first()
        return product

    @staticmethod
    async def get_product_by_id(product_id: int,
                             session: AsyncSession) -> Optional[Products]:
        query = await session.execute(select(Products).where(Products.id == product_id))
        product = query.scalars().first()
        return product

    @staticmethod
    async def get_all_products(session: AsyncSession) -> List[Products]:
        query = await session.execute(select(Products).order_by(Products.id))
        products = query.scalars().all()
        return products




    # @staticmethod
    # async def create_user(user_dto: ProductIn, plain_password, session: AsyncSession) -> User:
    #     user = User(**user_dto.model_dump())
    #     new_password = AuthService.get_password_hash(plain_password)
    #     user.password = new_password
    #     session.add(user)
    #     await session.commit()
    #     return user
