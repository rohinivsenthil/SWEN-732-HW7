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
    #TODO: define attributes for DVD

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
        #TODO: add code to check if book's is_available attribute is True 
        #(add print statmenets to let teh visitor know if the book is available or not)
        # if book.is_available:
        #     print(f"The book '{book.title}' is available in the library.")
        # else:
        #     print(f"The book '{book.title}' is not available in the library.")
        pass

    def visit_dvd(self, dvd):
        #TODO: add code to check if dvd is available, similar to visit_book
        pass

class LibraryCatalog:
    def __init__(self):
        self.library_items = []

    def add_item(self, item):
        self.library_items.append(item)

    def borrow_book(self, book_title):
        for item in self.library_items:
            if isinstance(item, Book) and item.title == book_title and item.is_available:
                item.is_available = False
                print(f"You have borrowed the book '{book_title}' from the library.")
                return
        print(f"The book '{book_title}' is not available in the library.")

    def borrow_dvd():
        #TODO: add code to set dvd available attribute to False, similar to borrow_book
        return
    
    def return_book():
        #TODO: add code to set available attribute of book back to True
        return
    
    def return_dvd():
        #TODO: add code to set available attribute of dvd back to True
        return


# Example Usage
if __name__ == "__main__":
    catalog = LibraryCatalog()
    catalog.add_item(Book("The Great Gatsby", "F. Scott Fitzgerald"))
    catalog.add_item(Book("To Kill a Mockingbird", "Harper Lee"))
    catalog.add_item(Book("1984", "George Orwell"))
    catalog.add_item(Book("The Catcher in the Rye", "J.D. Salinger"))
    catalog.add_item(Book("Pride and Prejudice", "Jane Austen"))

    book_to_borrow = "1984"
    catalog.borrow_book(book_to_borrow)
    catalog.borrow_book(book_to_borrow)  # Try to borrow the same book again

    #TODO: add more example usage for the TODO functions
