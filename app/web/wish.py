from . import web
from flask import flash, redirect, url_for, render_template
from flask_login import login_required, current_user
from app.models.base import db
from app.models.wish import Wish
from app.viewModels.wish import MyWishes

__author__ = '七月'


@web.route('/my/wish')
def my_wish():
    uid = current_user.id
    wish_of_mine = Wish.get_user_wish(uid)
    isbn_list = [wish.isbn for wish in wish_of_mine]
    gift_count_list = Wish.get_gift_count(isbn_list)
    view_model = MyWishes(wish_of_mine, gift_count_list)
    return render_template('my_wish.html', wishes=view_model.gifts)


@web.route('/wish/book/<isbn>')
@login_required
def save_to_wish(isbn):
    if current_user.can_save_to_list(isbn):
        with db.auto_commit():
            wish = Wish()
            wish.isbn = isbn
            wish.uid = current_user.id
            db.session.add(wish)
    else:
        flash('此书已存在您的心愿单或赠送单，请不要重复添加')
    return redirect(url_for('web.book_detail', isbn=isbn))


@web.route('/satisfy/wish/<int:wid>')
def satisfy_wish(wid):
    pass


@web.route('/wish/book/<isbn>/redraw')
def redraw_from_wish(isbn):
    pass
