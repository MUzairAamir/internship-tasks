class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"


class Member:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Library:

    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def show_books(self):
        print("Books:")

        for book in self.books:
            print(book)

    def show_members(self):
        print("Members:")

        for member in self.members:
            print(member)

    def __len__(self):
        return len(self.books)


# Creating Library
library = Library()

# Creating Books
book1 = Book("Python Basics", "Ali")
book2 = Book("OOP in Python", "Ahmed")

# Creating Members
member1 = Member("Uzair")
member2 = Member("Hamza")

# Adding books and members to Library
library.add_book(book1)
library.add_book(book2)

library.add_member(member1)
library.add_member(member2)

# Display
library.show_books()
library.show_members()

# Dunder method
print("Total books:", len(library))