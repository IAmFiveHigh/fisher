"""
  created by IAmFiveHigh on 2019-02-18
 """

from sqlalchemy import Column, Integer, SmallInteger
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True
    create_time = Column('create_time', Integer)
    status = Column(SmallInteger, default=1)
