from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from data_base import BaseSQLAlchemyModel


class DayResults(BaseSQLAlchemyModel):
    __tablename__ = "day_results"

    id_result = Column(Integer, autoincrement=True, primary_key=True )
    date = Column(String, nullable=False)
    get_in_day = Column(Integer, nullable=False)
    norma = Column(Integer, nullable=False)
    result = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("user.user_id"))

    user = relationship("User", back_populates="day_result")
    def __str__(self):
        return f"{self.user_id} {self.result}"

    def __repr__(self):
        return str(self)