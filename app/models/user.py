"""
  created by IAmFiveHigh on 2019-02-18
 """

from sqlalchemy import Column, Integer, String, Boolean, Float
from app.models.base import Base
from werkzeug.security import generate_password_hash, check_password_hash


class User(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    nickname = Column(String(24), nullable=False)
    _password = Column('password', String(128))
    phone_number = Column(String(18), unique=True)
    email = Column(String(50), unique=True, nullable=False)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)
    wx_open_id = Column(String(50))
    wx_name = Column(String(24))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def check_password(self, raw):
        # 第一个参数是加密后的 第二个是原始数据 相等返回True
        return check_password_hash(self._password, raw)