from pydantic import BaseModel


class DayResultIn(BaseModel):
    date : str
    get_in_day: int
    norma: int
    result: str
    user_id: int

    class Config:
        orm_mode: True