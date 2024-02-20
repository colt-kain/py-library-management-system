from book import Book
from library_member import LibraryMember

class Library:
    '''
    This class represents a library.

    Attributes:
        members_list (list[LibraryMember]): A list of all the library members.
        books_list (list[Book]): A list of all the books in the library.

    Methods:
        display_members(): Displays a list of all the members of the library.
        display_member_books(): Displays a list of all the books borrowed by a member.
        register_member(): Register a new member to the library.
        remove_member(): Remove a member from the existing members list.
        change_membership_status(): Change the membership status of a member.
    '''

    def __init__(self, members_list: list[LibraryMember],
                 books_list: list[Book]) -> None:
        self.members_list = members_list 
        self.books_list = books_list


    def display_members(self) -> None:
        for member in self.members_list:
            print(f'Member #[{member.member_id}] - {member.name}:')
            print(f'- Membership status: {member.membership_status}')
            print(f'- Contact information: {member.contact_information}\n')


    def display_member_books(self, member_id: int) -> None:
        if member_id not in [member.member_id for member in self.members_list]:
            print(f'Member #[{member_id}] not found.\n')
            return None

        for member in self.members_list:
            if member.member_id == member_id and len(member.books_borrowed) > 0:
                print(f'--- Books borrowed by {member.name} ---')
                for book in member.books_borrowed:
                    book.display_information()
                break
            else:
                print(f'Member #[{member_id}] has no borrowed books.\n')
                break


    def register_member(self, name: str, membership_status: str,
                        contact_information: str) -> None: 
        new_member = LibraryMember(name, len(self.members_list) + 1,
                                   membership_status, contact_information)
        self.members_list.append(new_member)


    def remove_member(self, member_id: int) -> None:
        if member_id not in [member.member_id for member in self.members_list]:
            print(f'Member #[{member_id}] not found.\n')
            return None

        # Create a list without the member marked for removal
        # then assign it as the new list.
        self.members_list = [member for member in self.members_list
            if member.member_id != member_id]

        # Update the member id for the remaining members.
        for i in range(len(self.members_list)):
            self.members_list[i].member_id = i + 1


    def change_membership_status(self, member_id: int,
                                 new_membership_status: str) -> None:
        if member_id not in [member.member_id for member in self.members_list]:
            print(f'Member #[{member_id}] not found.\n')
            return None

        if new_membership_status not in LibraryMember.membership_statuses:
            print('Invalid new membership status provided.\n')
            return None

        for member in self.members_list:
            if member.member_id == member_id:
                member.membership_status = new_membership_status
                break
