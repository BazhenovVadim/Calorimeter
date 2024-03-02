from pydantic import BaseModel


class ProductIn(BaseModel):
    product_name: str
    protein: str
    fats: str
    carbs: str
    calories: str

    class Config:
        orm_mode: True
