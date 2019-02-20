"""
  created by IAmFiveHigh on 2019-02-18
 """

from sqlalchemy import Column, Integer, String
from app.models.base import Base


class User(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    nickname = (String(50))

    def sample(self):
        pass