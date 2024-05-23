class Student:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        self.grades = []

    def addGrade(self, grade):
        self.grades.append(grade)

    def meanGrades(self):
        return sum(self.grades) / len(self.grades)

    def printInfo(self):
        print("Name:", self.name)
        print("Surname:", self.surname)
        print("Age:", self.age)
        print("Grades:", self.grades)


class Author:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def printInfo(self):
        print("Author:", self.name, self.surname)


class Book:
    def __init__(self, book_id, name, author):
        self.book_id = book_id
        self.name = name
        self.author = author
        self.is_borrowing = False

    def printInfo(self):
        print("Book ID:", self.book_id)
        print("Name:", self.name)
        self.author.printInfo()


class Library:
    def __init__(self):
        self.book_list = []
        self.student_list = []

    def add_book(self, book):
        self.book_list.append(book)

    def add_student(self, student):
        self.student_list.append(student)

    def borrow_book(self, student, book):
        if student in self.student_list and book in self.book_list:
            if book.is_borrowing == False and student.borrowing_count < 3:
                student.add_book(book)
                book.is_borrowing = True
                student.borrowing_count += 1
                print("Book borrowed successfully.")
            elif book.is_borrowing:
                print("This book is already borrowed.")
            elif student.borrowing_count >= 3:
                print("You have reached the maximum borrowing limit.")
        else:
            print("Student or book not found in the library.")

    def print_info(self):
        for student in self.student_list:
            student.print_info()


class Student:
    def __init__(self, student_id, full_name):
        self.student_id = student_id
        self.full_name = full_name
        self.borrowing_count = 0
        self.borrow_book_list = []

    def add_book(self, book):
        self.borrow_book_list.append(book)

    def print_info(self):
        print("Student ID:", self.student_id)
        print("Full Name:", self.full_name)
        print("Borrowing Count:", self.borrowing_count)
        print("Borrowed Books:")
        for book in self.borrow_book_list:
            book.printInfo()
            print()


# Example usage:

# Create Author
author1 = Author("J.K.", "Rowling")

# Create Book
book1 = Book(1, "Harry Potter and the Sorcerer's Stone", author1)

# Create Student
student1 = Student(1, "John Doe")

# Create Library
library = Library()

# Add book to library
library.add_book(book1)

# Add student to library
library.add_student(student1)

# Borrow book
library.borrow_book(student1, book1)

# Print student info
library.print_info()
