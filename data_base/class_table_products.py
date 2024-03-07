from sqlalchemy import Column, Integer, String,Float
from .database_meta import BaseSQLAlchemyModel


class Products(BaseSQLAlchemyModel):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String, nullable=False)
    proteins = Column(Float, nullable=False)
    fats = Column(Float, nullable=False)
    carbs = Column(Float, nullable=False)
    calories = Column(Float, nullable=False)

    def __str__(self):
        return f"{self.id}, {self.product_name}, {self.proteins}, {self.carbs}, {self.fats}, {self.calories}"

    def __repr__(self):
        return str(self)