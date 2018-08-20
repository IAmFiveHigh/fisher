"""
 created by wugao on 2018/8/19
"""

from flask import jsonify
from YuShu import YuShu
from help import is_isbn_or_key
from flask import Blueprint


__author__ = "IAmFiveHigh"

# 蓝图 blueprint
web = Blueprint('web', __name__)


@web.route('/book/search/<q>/<page>')
def search(q, page):
    """
        q :普通关键字 isbn
        page: 页码

    """
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShu.search_by_isbn(q)
    else:
        result = YuShu.search_by_keyword(q)

    return jsonify(result)


@web.route('/hello')
def hello():
    headers = {
        'content-type': 'text/html',
        # 'location': 'http://www.baidu.com'
    }
    # response = make_response('<html>hello</html>', 301)
    # response.headers = headers
    return '<html>hello</html>', 200
