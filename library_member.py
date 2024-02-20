from book import Book

class LibraryMember:
    '''
    This class represents a member of a library.

    Attributes:
        membership_statuses (list[str]): A list of all the available
            membership statuses.

        name (str): The name of the member.
        member_id (int): The identification code of the member.
        membership_status (str): The membership status of the member.
        contact_information (str): The member's contact information.
        books_borrowed (list[Book]): A list of the books borrowed by the member.

    Methods:
        borrow_book(): Borrow a book if it is available.
    '''

    membership_statuses = ['Regular', 'Student', 'Senior',
                           'Corporate', 'Guest', 'Online',
                           'Lifetime', 'Limited access', 'Suspended']


    def __init__(self, name: str, member_id: int, membership_status: str,
                 contact_information: str) -> None:
        self.name = name
        self.member_id = member_id
        self.membership_status = membership_status
        self.contact_information = contact_information
        self.books_borrowed = []


    def borrow_book(self, book: Book) -> None:
        if book.is_available:
            self.books_borrowed.append(book)
        else:
            print(f'[{book.isbn}] - "{book.title}" is not available.\n')

    
    def return_book(self, book: Book) -> None:
        self.books_borrowed.remove(book)
