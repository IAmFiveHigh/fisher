from flask import current_app

from app.libs.httper import HTTP
from app.models.book import Book

import mysql.connector
from app.secure import mysqlPassword


class YuShu:

    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    def __init__(self):
        self.total = 0
        self.books = []

    def search_by_isbn(self, isbn):
        url = self.isbn_url.format(isbn)
        result = HTTP.get(url)
        self.__fill_single(result)

    def search_by_keyword(self, key, page=1):

        url = self.keyword_url.format(key, current_app.config["PER_PAGE"], self.calculate_start(page))
        result = HTTP.get(url)
        self.__fill_collection(result)

    def __fill_single(self, data):
        if data:
            self.total = 1
            self.books.append(data)

    def __fill_collection(self, data):
        if data:
            self.total = data['total']
            self.books = data['books']

    @staticmethod
    def calculate_start(page):
        return (page-1) * current_app.config["PER_PAGE"]

    @staticmethod
    def create_book_model(json):
        model = Book(title=json['title'],
                     author=json['author'],
                     isbn=json['isbn'],
                     price=json['price'],
                     publisher=json['publisher'],
                     image=json['image'])
        return model

    @property
    def first(self):
        return self.books[0] if self.total > 0 else None



