# id, title, author, publish date, gener, available
BOOKS = (
    (1, "شازده کوچولو", "آنتوان دو سنت اگزوپری", 1943, "داستان", True),
    (2, "1984", "جورج اورول", 1949, "علمی-تخیلی", True),
    (3, "ثروت ملل", "آدام اسمیت", 1776, "اقتصاد", False),
    (4, "انسان خردمند", "یووال نوح هراری", 2011, "تاریخ", True),
    (5, "کیمیاگر", "پائولو کوئلیو", 1988, "داستان", True),
    (6, "صد سال تنهایی", "گابریل گارسیا مارکز", 1967, "داستان", False),
    (7, "هری پاتر و سنگ جادو", "جی. کی. رولینگ", 1997, "فانتزی", True),
    (8, "نبرد من", "آدولف هیتلر", 1925, "تاریخ", True),
    (9, "پدر پولدار پدر بی‌پول", "رابرت کیوساکی", 1997, "اقتصاد", True),
    (10, "دیوان حافظ", "حافظ شیرازی", 1390, "شعر", True)
)


def get_books(book_tupe) -> list:
    books = []
    for book in book_tupe:
        books.append( {
            "id": book[0],
            "title": book[1],
            "author": book[2],
            "publish_date": book[3],
            "gener": book[4],
            "is_available": book[5]

        })
    return books

def show_books(book_list: list):
    for book in book_list:
        print(book)

def sort_books(book_list: list, sort_by: str = "id", reverse = False):
    pass

book_list = get_books(BOOKS)

show_books(book_list)

