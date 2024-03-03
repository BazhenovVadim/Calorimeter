from pydantic import BaseModel


class DayResultIn(BaseModel):
    result: str
    user_id: int

    class Config:
        orm_mode: True