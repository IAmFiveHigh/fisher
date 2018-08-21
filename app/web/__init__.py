"""
  created by wugao on 2018-08-20
 """
from flask import Blueprint

__author__ = "IAmFiveHigh"

# 蓝图 blueprint
web = Blueprint('web', __name__)

from app.web import book
from app.web import user