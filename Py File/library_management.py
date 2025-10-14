class Book:
    def __init__(self,book_name,author,availability = True):
        self.name = book_name
        self.author = author
        self.status = availability

class Member:
    def __init__(self,member_name,member_id):
        self.name = member_name
        self.id = member_id
        self.books = []

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.load_books()
        self.load_members()
        self.load_borrowed()


    def add_book(self):
        book_name = input('Enter book name: ')
        author = input('Enter the name of the author: ')
        book = Book(book_name,author)
        self.books.append(book)

        with open('books.txt','a') as f:
            f.write(f'{book.name}|{book.author}|{book.status}\n')

        print(f'{book_name} by {author} added to the library')

    def add_member(self):
        member_name = input('Enter member name: ')
        member_id = input('Enter member ID: ')
        member = Member(member_name,member_id)
        self.members.append(member)

        with open('members.txt','a') as f:
            f.write(f'{member_name}|{member_id}\n')

        print(f'{member_name} with ID {member_id} added to the library')
    
    def display_books(self):
        print('\nBook List')
        for book in self.books:
            status = 'Available' if book.status == True else 'Borrowed'
            print(f'{book.name} by {book.author} - {status}')

    def display_members(self):
        print('\nMember List')
        for member in self.members:
            print(f'{member.name} (ID: {member.id})')
            if member.books:
                print('Borrowed Books: ')
                for book in member.books:
                    print(f'* {book.name} by {book.author}')
            else:
                print('No books borrowed')

    def save_book(self):
        with open('books.txt','w') as f:
            for book in self.books:
                f.write(f'{book.name}|{book.author}|{book.status}\n')

    def issue_book(self):
        print('\nBook issue procedure')
        member_id = input('Enter member ID: ')
        book_name = input('Enter book name to be issued: ')

        member = None
        for m in self.members:
            if m.id == member_id:
                member = m
                break
        if member is None:
            print('Member not found')
            return
        
        book = None
        for b in self.books:
            if b.name == book_name:
                book = b
                break
        if book is None:
            print('Book not found')
            return
            
        if book.status == False:
            print('Book is already issued')
            return

        with open('borrowed.txt', 'a') as f:
            f.write(f'{member.id}|{book.name}\n')
            
        book.status = False
        member.books.append(book)
        print(f'{book.name} issued to {member.name}')
        self.save_book()

    def return_book(self):
        print('\nBook return procedure')
        member_id = input('Enter member ID: ')
        book_name = input('Enter book name to return: ')

        member = None
        for m in self.members:
            if m.id == member_id:
                member = m
                break
        if member is None:
            print('Member not found')
            return
            
        book = None
        for b in self.books:
            if b.name == book_name:
                book = b
                break
        if book is None:
            print('Book not found')
            return
        
        if book.status == True:
            print(f'{book.name} is not currently issued')
            return
                
        book.status = True
        if book in member.books:
            member.books.remove(book)
        print(f'{book.name} returned by {member.name}')
        self.save_book()
        self.remove_borrowed(member.id, book.name)

    def load_borrowed(self):
        try:
            with open('borrowed.txt', 'r') as f:
                for line in f:
                    member_id, book_name = line.strip().split('|')

                    # Find the member and book objects
                    member = next((m for m in self.members if m.id == member_id), None)
                    book = next((b for b in self.books if b.name == book_name), None)

                    if member and book:
                        member.books.append(book)
        except FileNotFoundError:
            pass

    def remove_borrowed(self, member_id, book_name):
        try:
            with open('borrowed.txt', 'r') as f:
                lines = f.readlines()
            with open('borrowed.txt', 'w') as f:
                for line in lines:
                    if line.strip() != f'{member_id}|{book_name}':
                        f.write(line)
        except FileNotFoundError:
            pass

    def load_books(self):
        try:
            with open('books.txt','r') as f:
                for line in f:
                    line = line.strip()
                    name, author, status = line.split('|')
                    status = status == 'True'
                    self.books.append(Book(name, author, status))
        except FileNotFoundError:
            pass

    def load_members(self):
        try:
            with open('members.txt', 'r') as f:
                for line in f:
                    name, member_id = line.strip().split('|')
                    self.members.append(Member(name, member_id))
        except FileNotFoundError:
            pass

    def run(self):
        while True:
            print("\nLibrary Menu:")
            print("1. Add Book")
            print("2. Add Member")
            print("3. Display Books")
            print("4. Display Members")
            print("5. Issue Book")
            print("6. Return Book")
            print("7. Exit")
            
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.add_member()
            elif choice == '3':
                self.display_books()
            elif choice == '4':
                self.display_members()
            elif choice == '5':
                self.issue_book()
                self.save_book()
            elif choice == '6':
                self.return_book()
                self.save_book()
            elif choice == '7':
                print("Exiting")
                break
            else:
                print("Invalid choice. Please try again.")


library = Library()
library.run()