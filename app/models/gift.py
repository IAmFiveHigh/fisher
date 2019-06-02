"""
  created by IAmFiveHigh on 2019-02-22
 """

from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, desc, func
from app.models.base import Base, db
from app.models.wish import Wish
from sqlalchemy.orm import relationship
from flask import current_app
from app.spider.YuShu import YuShu

from collections import namedtuple

EachGiftWishCount = namedtuple('EachGiftWishCount', ['count', 'isbn'])


class Gift(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    launched = Column(Boolean, default=False)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    # book = relationship('Book')
    # bid = Column(Integer, ForeignKey('book.id'))

    @classmethod
    def get_user_gift(cls, uid):
        gifts = Gift.query.filter_by(
            uid=uid,
            launched=False
        ).order_by(
            desc(Gift.create_time)
        ).all()
        return gifts

    @classmethod
    def get_wish_count(cls, isbn_list):
        # 根据传入的一组isbn 到wish表中查询计算出某个礼物wish数量
        # filter里传入表达式
        # mysql in 查询
        # status == 1 因为之前的filter_by重写了 自动带status==1
        # isbn wish的数量
        count_wishs = db.session.query(func.count(Wish.id), Wish.isbn).filter(
            Wish.launched == False,
            Wish.isbn.in_(isbn_list),
            Wish.status == 1
        ).group_by(
            Wish.isbn
        ).all()
        count_list = [EachGiftWishCount(count=w[0], isbn=w[1]) for w in count_wishs]
        return count_list

    @property
    def book(self):
        yushu_book = YuShu()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first

    @classmethod
    def  recent(cls):
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