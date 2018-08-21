"""
 created by wugao on 2018/8/19
"""

from flask import jsonify, request
from YuShu import YuShu
from help import is_isbn_or_key
from app.forms.book import SearchForm
from . import web

__author__ = "IAmFiveHigh"


@web.route('/book/search')
def search():

    """
        q :普通关键字 isbn
        page: 页码

    """
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data

        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShu.search_by_isbn(q)
        else:
            result = YuShu.search_by_keyword(q, page)

        return jsonify(result)
    else:
        return jsonify(form.errors)


@web.route('/hello')
def hello():
    headers = {
        'content-type': 'text/html',
        # 'location': 'http://www.baidu.com'
    }
    # response = make_response('<html>hello</html>', 301)
    # response.headers = headers
    return '<html>hello</html>', 200
