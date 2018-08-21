"""
  created by wugao on 2018-08-21
 """

from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired

__author__ = "IAmFiveHigh"


class SearchForm(Form):
    q = StringField(validators=[Length(min=1, max=30), DataRequired()])
    page = IntegerField(validators=[NumberRange(min=1, max=99, message="page超出范围")], default=1)