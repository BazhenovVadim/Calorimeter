from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from data_base import Base


class DayResults(Base):
    __tablename__ = "day_results"

    id_result = Column(Integer, autoincrement=True, primary_key=True )
    result = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("user.user_id"), nullable=False)

    user = relationship("User", back_populates="day_result")
    def __str__(self):
        return f"{self.user_id} {self.result}"

    def __repr__(self):
        return str(self)