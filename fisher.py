"""
 created by wugao on 2018/8/18
"""

from flask import Flask

from YuShu import YuShu
from help import is_isbn_or_key

import json

__author__ = 'IAmFiveHigh'

app = Flask(__name__)
app.config.from_object('config')


@app.route('/book/search/<q>/<page>')
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

    return json.dump(result), 200, {'content-type': 'application/json'}


@app.route('/helloo')
def helloo():
    headers = {
        'content-type': 'text/plain',
        'location': 'http://www.baidu.com'
    }
    # response = make_response('<html>hello</html>', 301)
    # response.headers = headers
    return '<html>hello</html>', 301, headers


if __name__ == '__main__':
    # debug = true 自动重启服务器
    app.run(host='0.0.0.0', debug=app.config['DEBUG'])

