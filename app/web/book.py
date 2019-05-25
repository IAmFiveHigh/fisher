"""
 created by wugao on 2018/8/19
"""

from flask import jsonify, request, render_template, flash
from flask_login import current_user
from app.forms.book import SearchForm
from app.libs.help import is_isbn_or_key
from app.spider.YuShu import YuShu
from . import web
from app.models.gift import Gift
from app.models.wish import Wish
from app.viewModels.trade import TradeInfo
from app.viewModels.book import BookCollection, BookViewModel

import json

__author__ = "IAmFiveHigh"


@web.route('/book/search')
def search():
    """
        q :普通关键字 isbn
        page: 页码

    """
    form = SearchForm(request.args)
    # result = {
    #     'code': 0,
    #     'message': '正确返回数据'
    # }
    books = BookCollection()
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data

        yushu = YuShu()
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            yushu.search_by_isbn(q)
        else:
            yushu.search_by_keyword(q, page)
        books.fill(yushu, q)

        # # 先把对象转换成json字符串 再用loads方法转换成dict
        # data_string = json.dumps(books, default=lambda o: o.__dict__)
        # result['data'] = json.loads(data_string)

        # return jsonify(result)
    else:
        # result['code'] = 1
        # result['message'] = form.errors
        # return jsonify(result)
        flash('搜索关键词不符合要求，请重新输入关键词')
    return render_template('search_result.html', books=books, form=form)


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    # 默认不在礼物清单 也不在心愿单
    has_in_gifts = False
    has_in_wishes = False

    # 取书籍详情数据
    yushu_book = YuShu()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModel(yushu_book.first)

    if current_user.is_authenticated:
        if Gift.query.filter_by(isbn=isbn, uid=current_user.id, launched=False).first():
            has_in_gifts = True
        if Wish.query.filter_by(isbn=isbn, uid=current_user.id, launched=False).first():
            has_in_wishes = True

    trade_gifts = Gift.query.filter_by(isbn=isbn, launched=False).all()
    trade_wishes = Wish.query.filter_by(isbn=isbn, launched=False).all()

    trade_gifts_model = TradeInfo(trade_gifts)
    trade_wishes_model = TradeInfo(trade_wishes)

    return render_template('book_detail.html',
                           book=book,
                           wishes=trade_wishes_model,
                           gifts=trade_gifts_model,
                           has_in_gifts=has_in_gifts,
                           has_in_wishes=has_in_wishes)
