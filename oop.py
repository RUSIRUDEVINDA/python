class Book:
    def __init__(self,title,author,isbn):

        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed: 
          self.is_borrowed = True
          return True
        return False

    def return_book(self):
        self.is_borrowed = False

#class member

class Member:
    def __init__(self,name,member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = [] #List of borrowed books

    def borrow_book(self,book):
        if book.borrow():
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed {book.title}")
        else:
            print(f"{book.title} is already borrowed")
    
    def return_book(self,book):
        book.return_book()
        self.borrowed_books.remove(book)
        print(f"{self.name} return {book.title}")

#class library

class Library:
    def __init__(self):
        self.book = []
        self.members = []

    def add_book(self,book):
        self.book.append(book)

    def add_member(self,member):
        self.members.append(member)

    def show_available_books(self):
        for book in self.book:
            if not book.is_borrowed:
                print(f"{book.title} by {book.author}")

lib = Library()
b1 = Book("Harry Potter", "J.K Rowling","1001")
b2 = Book("Atomic Habbits", "Jami lanister","1002")

lib.add_book(b1)
lib.add_book(b2)

m1 = Member("Alice","M001")
m2 = Member("Sam","M001")

lib.show_available_books()
m1.borrow_book(b1)
lib.show_available_books


