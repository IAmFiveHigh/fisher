"""
  created by IAmFiveHigh on 2018-09-26
 """


class BookViewModel:
    @classmethod
    def package_single(cls, data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }

        if data:
            returned['total'] = 1
            returned['books'] = cls.__cut_book_detail(data)
        return returned

    @classmethod
    def package_collection(cls, data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = data['total']
            returned['books'] = [cls.__cut_book_detail(book) for book in data['books']]
        return returned

    @classmethod
    def __cut_book_detail(cls, data):
        book = {
            'title': data['title'],
            'publisher': data['publisher'],
            'pages': data['pages'],
            'price': data['price'],
            'summary': data['summary'],
            'image': data['image'],
            'author': '、'.join(data['author'])
        }
        return book
