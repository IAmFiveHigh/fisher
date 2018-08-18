"""
 created by wugao on 2018/8/18
"""

from flask import Flask, make_response

__author__ = 'IAmFiveHigh'

app = Flask(__name__)
app.config.from_object('config')


@app.route('/hello')
def hello():
    return 'hello wugao'


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

