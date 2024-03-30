from typing import Optional, List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from data_base import DayResults


class DayResultService:
    @staticmethod
    async def get_result_by_user_id(user_id:int, session: AsyncSession) -> List[DayResults]:
        query = await session.execute(select(DayResults).where(DayResults.user_id == user_id))
        day_result = query.scalars().first()
        return day_result

    @staticmethod
    async def get_all_results(user_id: int, session: AsyncSession) -> List[DayResults]:
        query = await session.execute(select(DayResults).where(DayResults.user_id == user_id).order_by(DayResults.id_result))
        results = query.scalars().all()
        return results



