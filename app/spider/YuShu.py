from flask import current_app

from app.libs.httper import HTTP
from app.models.book import db, Book

import mysql.connector
from app.secure import mysqlPassword

class YuShu:

    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        result = HTTP.get(url)
        # db.session.add(YuShu.create_book_model(result))
        # db.session.commit()
        # YuShu.create_book_models_by_mysql(result)

        return YuShu.search_book_by(isbn)

    @classmethod
    def search_by_keyword(cls, key, page=1):

        url = cls.keyword_url.format(key, current_app.config["PER_PAGE"], cls.calculate_start(page))
        result = HTTP.get(url)
        return result

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

    @staticmethod
    def create_book_models_by_mysql(json):
        conn = mysql.connector.connect(user='root', password=mysqlPassword, database='fisher')
        cursor = conn.cursor()
        cursor.execute('insert into book (title, isbn, price, publisher, image, summary) values (%s, %s, %s, %s, %s, %s)',
                       [json['title'], json['isbn'], json['price'], json['publisher'], json['image'], json['summary']])
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def search_book_by(isbn):
        conn = mysql.connector.connect(user='root', password=mysqlPassword, database='fisher')
        cursor = conn.cursor()
        cursor.execute('select * from book where isbn = %s', (isbn, ))
        values = cursor.fetchall()
        cursor.close()
        conn.close()

        return values