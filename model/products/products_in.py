from pydantic import BaseModel


class ProductIn(BaseModel):
    product_name: str
    protein: float
    fats: float
    carbs: float
    calories: float

    class Config:
        orm_mode: True
