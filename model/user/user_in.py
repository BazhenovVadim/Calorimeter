from pydantic import BaseModel


class UserIn(BaseModel):
    user_id: str
    login: str
    email: str

    class Config:
        orm_mode: True
