from model.day_result.day_result_in import DayResultIn


class DayResultOut(DayResultIn):
    id_result: int

    class Config:
        orm_mode: True
