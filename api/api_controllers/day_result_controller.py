from typing import Optional, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from data_base import DayResults, get_session, User
from model import DayResultOut
from services import DayResultService, AuthService

router = APIRouter(prefix="/day_results", tags=["day_results"])


@router.get("/{day_result}", response_model=Optional[DayResultOut])
async def get_result_by_user_id(user_id: int, session: AsyncSession = Depends(get_session)):
    result = await DayResultService.get_result_by_user_id(user_id, session)
    if result:
        dto_result = DayResultOut(**result.to_dict())
        return dto_result
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Не найден результат с таким айди пользователя")


@router.get("/", response_model=List[DayResultOut])
async def get_all_results(current_user: User = Depends(AuthService.get_current_user),
                          session: AsyncSession = Depends(get_session)):
    results = await DayResultService.get_all_results(current_user.user_id, session)
    return list(map(lambda x: DayResultOut(**x.to_dict()), results))
