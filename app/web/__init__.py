"""
  created by wugao on 2018-08-20
 """
from flask import Blueprint

__author__ = "IAmFiveHigh"

# 蓝图 blueprint
web = Blueprint('web', __name__)

from app.web import book
from app.web import auth
from app.web import drift
from app.web import gift
from app.web import main
from app.web import wish
from app.web import test
