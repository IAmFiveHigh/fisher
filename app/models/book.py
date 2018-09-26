"""
  created by wugao on 2018-08-22
 """

from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy

__author__ = "IAmFiveHigh"

db = SQLAlchemy()


class Book(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(20), default='未名')
    isbn = Column(String(15), nullable=False, unique=True)
    price = Column(String(20))
    publisher = Column(String(50))
    image = Column(String(50))
    pages = Column(Integer)
    binding = Column(String(20))
    pubdate = Column(String(20))
    summary = Column(String(1000))

    def sample(self):
        pass