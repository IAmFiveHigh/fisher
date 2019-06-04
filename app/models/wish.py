"""
  created by IAmFiveHigh on 2019-02-25
 """

from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, desc, func
from app.models.base import Base, db
from sqlalchemy.orm import relationship
from app.spider.YuShu import YuShu


class Wish(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    launched = Column(Boolean, default=False)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    # book = relationship('Book')
    # bid = Column(Integer, ForeignKey('book.id'))

    @classmethod
    def get_user_wish(cls, uid):
        wishes = Wish.query.filter_by(
            uid=uid,
            launched=False
        ).order_by(
            desc(Wish.create_time)
        ).all()
        return wishes

    @classmethod
    def get_gift_count(cls, isbn_list):
        # 根据传入的一组isbn 到wish表中查询计算出某个礼物wish数量
        # filter里传入表达式
        # mysql in 查询
        # status == 1 因为之前的filter_by重写了 自动带status==1
        # isbn wish的数量
        from .gift import Gift
        count_gifts = db.session.query(func.count(Gift.id), Wish.isbn).filter(
            Gift.launched == False,
            Gift.isbn.in_(isbn_list),
            Gift.status == 1
        ).group_by(
            Gift.isbn
        ).all()
        from .gift import EachGiftWishCount
        count_list = [EachGiftWishCount(count=w[0], isbn=w[1]) for w in count_gifts]
        return count_list

    @property
    def book(self):
        yushu_book = YuShu()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first
