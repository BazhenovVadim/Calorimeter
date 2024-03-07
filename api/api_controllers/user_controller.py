from typing import Optional, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from data_base import get_session
from model import UserOut
from services import UserService

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/{id}", response_model=Optional[UserOut])
async def get_user(user_id: int, session: AsyncSession = Depends(get_session)):
    user = await UserService.get_user_by_id(user_id, session)
    if user:
        dto_user = UserOut(**user.to_dict())
        return dto_user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id {user_id} not found!")


@router.get("/", response_model=List[UserOut])
async def get_users(session: AsyncSession = Depends(get_session)):
    users = await UserService.get_all_users(session)
    return list(map(lambda x: UserOut(**x.to_dict()), users))

@router.post("/",response_model=UserOut)
async def create_user(user_dto:UserOut, plain_password:str, session:AsyncSession = Depends(get_session)):
    new_user = await UserService.create_user(user_dto, plain_password, session)
    return UserOut(**new_user.to_dict())

@router.put("/", response_model=UserOut)
async def update_user(user_dto:UserOut, session:AsyncSession = Depends(get_session)):
    user = await UserService.get_user_by_id(user_dto.id, session)
    if user:
        user.update(user_dto.model_dump(exclude={"id"}))
        await session.commit()
        return UserOut(**user.to_dict())
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with id {user_dto.id} not found!")

@router.delete("/")
async def delete_user(user_id: int, session: AsyncSession = Depends(get_session)):
    user = await UserService.get_user_by_id(user_id, session)
    if user:
        await session.delete(user)
        await session.commit()
        return "status OK"
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id {user_id} not found!")
