BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]

from Lab2_T1 import *

class Library:
    books = []

    def __init__(self, books = None):
        self.books = books
        if books == None: self.books = []

    def get_next_book_id(self) -> int:
        return len(self.books)+1

    def get_index_by_book_id(self, id):
        for a in enumerate(self.books):
            if (id == a[0]):
                return a[0]
        raise ValueError("Книги с данным id не существует")

if __name__ == '__main__':
    empty_library = Library()
    print(empty_library.get_next_book_id())

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)
    print(library_with_books.get_next_book_id())

    print(library_with_books.get_index_by_book_id(1))