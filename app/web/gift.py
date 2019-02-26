
from . import web
from app.models.base import db
from flask import current_app, flash, url_for, redirect
from flask_login import login_required, current_user
from app.models.gift import Gift

__author__ = '七月'


@web.route('/my/gifts')
@login_required
def my_gifts():
    return 'My Gifts'


@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    if current_user.can_save_to_list(isbn):
        # try:
        with db.auto_commit():
            gift = Gift()
            gift.user = current_user
            gift.isbn = isbn
            current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
            db.session.add(gift)
            # db.session.commit()
            # 上面整段数据库操作代码在commit才真正执行
        # except Exception as e:
        #     # 如果 上面代码出错 就回滚
        #     db.session.rollback()
        #     raise e
    else:
        flash('此书已存在您的心愿单或赠送单，请不要重复添加')
    return redirect(url_for('web.book_detail', isbn=isbn))


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass



