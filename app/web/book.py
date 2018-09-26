"""
 created by wugao on 2018/8/19
"""

from flask import jsonify, request

from app.forms.book import SearchForm
from app.libs.help import is_isbn_or_key
from app.spider.YuShu import YuShu
from . import web
from app.viewModels.book import BookViewModel

__author__ = "IAmFiveHigh"


@web.route('/book/search')
def search():

    """
        q :普通关键字 isbn
        page: 页码

    """
    form = SearchForm(request.args)
    json = {
        'code': 0,
        'message': '正确返回数据'
    }
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data

        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShu.search_by_isbn(q)
            result = BookViewModel.package_single(result, q)

        else:
            result = YuShu.search_by_keyword(q, page)
            result = BookViewModel.package_collection(result, q)
        json['data'] = result

        return jsonify(json)
    else:
        json['code'] = 1
        json['message'] = form.errors
        return jsonify(json)


@web.route('/hello')
def hello():
    headers = {
        'content-type': 'text/html',
        # 'location': 'http://www.baidu.com'
    }
    # response = make_response('<html>hello</html>', 301)
    # response.headers = headers
    return '<html><h1>hello</h1><p>are you OK?</p></html>', 200
