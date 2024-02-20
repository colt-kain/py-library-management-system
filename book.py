class Book:
    """
    This class represents a book inside of a library.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        isbn (str): The International Standard Book Number.
        genre (str): The genre of the book.
        publication_year (int): The year when the book was published.
        pages_number (int): The total number of pages in the book.
        is_available (bool): Indicates whether the book is available for checkout.

    Methods:
        display_information(): Displays detailed information about the book.
    """


    def __init__(
        self,
        title: str,
        author: str,
        isbn: str,
        genre: str,
        publication_year: int,
        pages_number: int,
        is_available: bool
    ) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.publication_year = publication_year
        self.pages_number = pages_number
        self.is_available = is_available


    def display_information(self) -> None:
        print(f'[{self.isbn}] - "{self.title}" ({self.publication_year}):')
        print(f'* Author: {self.author}')
        print(f'* Genre: {self.genre}')
        print(f'* Number of pages: {self.pages_number}')
        print()
