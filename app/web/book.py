"""
 created by wugao on 2018/8/19
"""

from flask import jsonify, request

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
    result = {
        'code': 0,
        'message': '正确返回数据'
    }
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data

        books = BookCollection()
        yushu = YuShu()
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            yushu.search_by_isbn(q)
        else:
            yushu.search_by_keyword(q, page)
        books.fill(yushu, q)

        # 先把对象转换成json字符串 再用loads方法转换成dict
        data_string = json.dumps(books, default=lambda o: o.__dict__)
        result['data'] = json.loads(data_string)

        return jsonify(result)
    else:
        result['code'] = 1
        result['message'] = form.errors
        return jsonify(result)


@web.route('/hello')
def hello():
    headers = {
        'content-type': 'text/html',
        # 'location': 'http://www.baidu.com'
    }
    # response = make_response('<html>hello</html>', 301)
    # response.headers = headers
    return '<html><h1>hello</h1><p>are you OK?</p></html>', 200
