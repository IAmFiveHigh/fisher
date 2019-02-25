"""
  created by IAmFiveHigh on 2019-02-25
 """

from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from app.models.base import Base
from sqlalchemy.orm import relationship


class Wish(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    launched = Column(Boolean, default=False)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    # book = relationship('Book')
    # bid = Column(Integer, ForeignKey('book.id'))