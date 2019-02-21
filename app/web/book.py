"""
 created by wugao on 2018/8/19
"""

from flask import jsonify, request, render_template, flash

from app.forms.book import SearchForm
from app.libs.help import is_isbn_or_key
from app.spider.YuShu import YuShu
from . import web
from app.viewModels.book import BookCollection

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
    return render_template('search_result.html', books=books)


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    pass

