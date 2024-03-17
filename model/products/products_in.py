from pydantic import BaseModel


class ProductIn(BaseModel):
    product_name: str
    proteins: float
    fats: float
    carbs: float
    calories: float

    class Config:
        orm_mode: True
