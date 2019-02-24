"""
  created by wugao on 2018-08-20
 """
from flask import Flask
from app.models.base import db
from flask_login import LoginManager

__author__ = "IAmFiveHigh"

login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)

    db.init_app(app)
    db.create_all(app=app)

    login_manager.init_app(app=app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录'
    return app


def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)