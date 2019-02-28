"""
  created by IAmFiveHigh on 2019-02-22
 """

from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, desc
from app.models.base import Base
from sqlalchemy.orm import relationship
from flask import current_app
from app.spider.YuShu import YuShu


class Gift(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    launched = Column(Boolean, default=False)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    # book = relationship('Book')
    # bid = Column(Integer, ForeignKey('book.id'))

    @property
    def book(self):
        yushu_book = YuShu()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first

    @classmethod
    def recent(cls):
        recent_gifts = Gift.query.filter_by(
            launched=False
        ).group_by(
            Gift.isbn
        ).order_by(
            desc(Gift.create_time)
        ).limit(
            current_app.config['RECENT_BOOK_LIMIT']
        ).distinct().all()
        return recent_gifts