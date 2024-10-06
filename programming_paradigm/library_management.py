class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        self._is_checked_out = True

    def return_book(self):
        self._is_checked_out = False

    def is_available(self):
        return not self._is_checked_out

class Library:
    def __init__(self):
        self._books = []

    def add_book(self,book):
        self._books.append(book)

    def return_book(self,title):
        for book in self._books:
            if book.title == title:
                self._books.remove(book)

    def check_out_book(self,title):
        for book in self._books:
            if book.title == title:
                book._is_checked_out = True
                return f"{title} is found"
            else:
                return f"{title} is not found"
    def list_available_books(self):
        for book in self._books:
             print(f"{book.title} by {book.author}")