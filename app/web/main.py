from . import web
from flask import render_template
from app.models.gift import Gift
from app.viewModels.book import BookViewModel

__author__ = '七月'


@web.route('/')
def index():
    recent_gifts = Gift.recent()
    books = [BookViewModel(gift.book) for gift in recent_gifts]
    return render_template('index.html', recents=books)


@web.route('/personal')
def personal_center():
    pass
