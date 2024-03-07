from typing import Optional, List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from data_base import User
from model import UserIn
from services import AuthService


class UserService:
    @staticmethod
    async def get_user_by_id(user_id:int,
                             session: AsyncSession) -> Optional[User]:
        query = await session.execute(select(User).where(User.user_id == user_id))
        user = query.scalars().first()
        return user

    @staticmethod
    async def get_user_by_login(login: str,
                                session: AsyncSession) -> Optional[User]:
        query = await session.execute(select(User).where(User.login == login))
        login = query.scalars().first()
        return login

    @staticmethod
    async def get_all_users(session: AsyncSession) -> List[User]:
        query = await session.execute(select(User))
        users = query.scalars().all()
        return users

    @staticmethod
    async def create_user(user_dto: UserIn, plain_password, session :AsyncSession) -> User:
        user = User(**user_dto.model_dump())
        new_password = AuthService.get_password_hash(plain_password)
        user.password = new_password
        session.add(user)
        await session.commit()
        return user