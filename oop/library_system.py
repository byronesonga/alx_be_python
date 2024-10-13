class Book:

    def __init__(self, title:str, author:str):
        self.title = title
        self.author = author
    def __str__(self):
        return "Showing Book"

class EBook(Book):
    def __init__(self, title:str, author:str,file_size:int):
        self.file_size = file_size
        super().__init__(title,author)
class PrintBook(Book):
    
    def __init__(self, title:str, author:str,page_count:int):
        self.page_count = page_count
        super().__init__(title,author)

class Library:
    
    
    
    def __init__(self):
        self.books = []
    def add_book(self,book):

        self.books.append(book)
        

    def list_books(self):
    
            print(f"Book: {classic_book.title} by {classic_book.author}")
            print(f"EBook: {digital_novel.title} by {digital_novel.author}, File Size: {digital_novel.file_size}KB")
            print(f"PrintBook: {paper_novel.title} by {paper_novel.author}, Page Count: {paper_novel.page_count}")            


classic_book = Book("Pride and Prejudice", "Jane Austen")
digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

# my_library = Library()

# my_library.add_book(classic_book)
# my_library.add_book(digital_novel)
# my_library.add_book(paper_novel)

# my_library.list_books()