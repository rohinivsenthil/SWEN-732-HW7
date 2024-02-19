from abc import ABC, abstractmethod

class LibraryItem(ABC):
    """Abstract base class for library items."""

    @abstractmethod
    def accept(self, visitor):
        """Accept method for visitor pattern."""
        pass

class Book(LibraryItem):
    """Class representing a book in the library."""

    def __init__(self, title, author):
        """
        Initialize a book.

        Parameters:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author
        self.is_available = True

    def accept(self, visitor):
        """
        Accept method for visitor pattern.

        Parameters:
            visitor (Visitor): The visitor object.
        """
        visitor.visit_book(self)

class DVD(LibraryItem):
    """Class representing a DVD in the library."""

    def __init__(self, title, director):
        """
        Initialize a DVD.

        Parameters:
            title (str): The title of the DVD.
            director (str): The director of the DVD.
        """
        self.title = title
        self.director = director
        self.is_available = True

    def accept(self, visitor):
        """
        Accept method for visitor pattern.

        Parameters:
            visitor (Visitor): The visitor object.
        """
        visitor.visit_dvd(self)

class Visitor(ABC):
    """Abstract base class for visitors."""

    @abstractmethod
    def visit_book(self, book):
        """Visit method for books."""
        pass

    @abstractmethod
    def visit_dvd(self, dvd):
        """Visit method for DVDs."""
        pass

class LibraryVisitor(Visitor):
    """Visitor class for checking availability of items."""

    def visit_book(self, book):
        """
        Visit method for books.

        Parameters:
            book (Book): The book to visit.
        """
        if book.is_available:
            print(f"The book '{book.title}' is available in the library.")
        else:
            print(f"The book '{book.title}' is not available in the library.")

    def visit_dvd(self, dvd):
        """
        Visit method for DVDs.

        Parameters:
            dvd (DVD): The DVD to visit.
        """
        if dvd.is_available:
            print(f"The DVD '{dvd.title}' is available in the library.")
        else:
            print(f"The DVD '{dvd.title}' is not available in the library.")

class LibraryCatalog:
    """Class representing a library catalog."""

    def __init__(self):
        """Initialize the library catalog."""
        self.items = []

    def add_book(self, item):
        """
        Add a book to the library catalog.

        Parameters:
            item (Book): The book to add.
        """
        self.items.append(item)

    def add_dvd(self, item):
        """
        Add a DVD to the library catalog.

        Parameters:
            item (DVD): The DVD to add.
        """
        self.items.append(item)

    def borrow_book(self, book_title):
        """
        Borrow a book from the library.

        Parameters:
            book_title (str): The title of the book to borrow.
        """
        for item in self.items:
            if isinstance(item, Book) and item.title == book_title and item.is_available:
                item.is_available = False
                print(f"You have borrowed the book '{book_title}' from the library.")
                return
        print(f"The book '{book_title}' is not available in the library.")

    def borrow_dvd(self, dvd_title):
        """
        Borrow a DVD from the library.

        Parameters:
            dvd_title (str): The title of the DVD to borrow.
        """
        for item in self.items:
            if isinstance(item, DVD) and item.title == dvd_title and item.is_available:
                item.is_available = False
                print(f"You have borrowed the DVD '{dvd_title}' from the library.")
                return
        print(f"The DVD '{dvd_title}' is not available in the library.")
    
    def return_book(self, book_title):
        """
        Return a book to the library.

        Parameters:
            book_title (str): The title of the book to return.
        """
        for item in self.items:
            if isinstance(item, Book) and item.title == book_title and not item.is_available:
                item.is_available = True
                print(f"The book '{book_title}' is returned to the library.")
                return
        print(f"The book '{book_title}' is already in the library.")

    def return_dvd(self, dvd_title):
        """
        Return a DVD to the library.

        Parameters:
            dvd_title (str): The title of the DVD to return.
        """
        for item in self.items:
            if isinstance(item, DVD) and item.title == dvd_title and not item.is_available:
                item.is_available = True
                print(f"The DVD '{dvd_title}' is returned to the library.")
                return
        print(f"The DVD '{dvd_title}' is already in the library.")


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
