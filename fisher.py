"""
 created by wugao on 2018/8/18
"""

from flask import Flask, jsonify

from app import create_app

__author__ = 'IAmFiveHigh'


app = create_app()

if __name__ == '__main__':
    # debug = true 自动重启服务器
    app.run(host='0.0.0.0', debug=app.config['DEBUG'])

