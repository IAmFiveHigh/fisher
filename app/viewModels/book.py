"""
  created by IAmFiveHigh on 2018-09-26
 """


class BookViewModel:
    def __init__(self, book):
        self.title = book['title']
        self.publisher = book['publisher']
        self.pages = book['pages']
        self.price = book['price']
        self.summary = book['summary']
        self.image = book['image']
        self.author = book['author']


class BookCollection:
    def __init__(self):
        self.total = 0
        self.keyword = ''
        self.books = []

    def fill(self, yushu_book, keyword):
        self.total = yushu_book.total
        self.keyword = keyword
        self.books = [BookViewModel(book) for book in yushu_book.books]


class _BookViewModel:
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
