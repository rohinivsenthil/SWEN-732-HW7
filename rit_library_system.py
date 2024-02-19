from abc import ABC, abstractmethod

# Element Interface
class LibraryItem(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

# Concrete Elements
class Book(LibraryItem):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def accept(self, visitor):
        visitor.visit_book(self)

class DVD(LibraryItem):
    def __init__(self, title, director):
        self.title = title
        self.director = director
        self.is_available = True

    def accept(self, visitor):
        visitor.visit_dvd(self)

# Visitor Interface
class Visitor(ABC):
    @abstractmethod
    def visit_book(self, book):
        pass

    @abstractmethod
    def visit_dvd(self, dvd):
        pass

# Concrete Visitors
class LibraryVisitor(Visitor):
    def visit_book(self, book):
        if book.is_available:
            print(f"The book '{book.title}' is available in the library.")
        else:
            print(f"The book '{book.title}' is not available in the library.")

    def visit_dvd(self, dvd):
        if dvd.is_available:
            print(f"The DVD '{dvd.title}' is available in the library.")
        else:
            print(f"The DVD '{dvd.title}' is not available in the library.")

class LibraryCatalog:
    def __init__(self):
        self.items = []

    def add_book(self, item):
        self.items.append(item)

    def add_dvd(self, item):
        self.items.append(item)

    def borrow_book(self, book_title):
        for item in self.items:
            if isinstance(item, Book) and item.title == book_title and item.is_available:
                item.is_available = False
                print(f"You have borrowed the book '{book_title}' from the library.")
                return
        print(f"The book '{book_title}' is not available in the library.")

    def borrow_dvd(self, dvd_title):
        for item in self.items:
            if isinstance(item, DVD) and item.title == dvd_title and item.is_available:
                item.is_available = False
                print(f"You have borrowed the DVD '{dvd_title}' from the library.")
                return
        print(f"The DVD '{dvd_title}' is not available in the library.")
    
    def return_book(self, book_title):
        for item in self.items:
            if isinstance(item, Book) and item.title == book_title and item.is_available == False:
                item.is_available = True
                print(f"The book '{book_title}' is returned to the library.")
                return
        print(f"The book '{book_title}' is already in the library.")

    def return_dvd(self, dvd_title):
        for item in self.items:
            if isinstance(item, Book) and item.title == dvd_title and item.is_available == False:
                item.is_available = True
                print(f"The book '{dvd_title}' is returned to the library.")
                return
        print(f"The book '{dvd_title}' is already in the library.")


# Example Usage
if __name__ == "__main__":
    catalog = LibraryCatalog()
    catalog.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald"))
    catalog.add_book(Book("To Kill a Mockingbird", "Harper Lee"))
    catalog.add_book(Book("1984", "George Orwell"))

    book = "1984"
    catalog.borrow_book(book)
    catalog.borrow_book(book)  # Try to borrow the same book again
    catalog.return_book(book)
    catalog.borrow_book(book)

   
