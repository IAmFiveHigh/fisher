"""
  created by IAmFiveHigh on 2019-02-22
 """

from wtforms import Form, StringField, IntegerField, PasswordField
from wtforms.validators import Length, NumberRange, DataRequired, Email, ValidationError
from app.models.user import User


class RegisterForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64), Email(message='电子邮箱不符合规范')])

    password = PasswordField(validators=[
        DataRequired(message='密码不能为空,请输入密码'), Length(6, 32)
    ])

    nickname = StringField(validators=[DataRequired(), Length(2, 10, message='昵称最少两字符，最多10字符')])

    # 只要是 validate带 email自动找到email成员变量
    def validate_email(self, filed):
        if User.query.filter_by(email=filed.data).first():
            raise ValidationError('电子邮箱已被注册')

    def validate_nickname(self, filed):
        if User.query.filter_by(nickname=filed.data).first():
            raise ValidationError('昵称已被注册')


class LoginForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64), Email(message='电子邮箱不符合规范')])

    password = PasswordField(validators=[
        DataRequired(message='密码不能为空,请输入密码'), Length(6, 32)
    ])