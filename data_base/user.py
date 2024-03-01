from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from data_base import Base


class User(Base):
    __tablename__ = "user"

    user_id = Column(Integer,autoincrement=True, primary_key=True)
    user_name = Column(String, nullable=False)
    login = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)

    day_result = relationship("DayResults", back_populates="user")

    def __str__(self):
        return f"{self.user_id} {self.user_name} {self.login}"

    def __repr__(self):
        return str(self)
