from typing import AsyncIterator

from pydantic import BaseModel
from sqlalchemy import inspect, create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
from config import DATABASE_HOST, DATABASE_USER, DATABASE_PASSWORD, DATABASE_NAME, DATABASE_PORT, SQL_ECHO

Base = declarative_base()
engine_async = create_async_engine(
    f"postgresql+asyncpg://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}",
    echo=SQL_ECHO,
    future=True)
session_async_factory = sessionmaker(engine_async, class_=AsyncSession,
                                     expire_on_commit=False,
                                     autoflush=False)
engine = create_engine(f"postgresql+psycopg2://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}", echo=False)
session_factory = sessionmaker(engine, autocommit=False)
metadata = Base.metadata


class BaseSQLAlchemyModel(Base):
    __abstract__ = True

    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}

    def update(self, model: dict):
        for key, value in model.items():
            setattr(self, key, value)


async def get_session() -> AsyncIterator[AsyncSession]:
    async with session_async_factory() as session:
        yield session
