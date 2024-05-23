# class Author:
#     def __init__(self, name, surname, id):
#         self.id = id
#         self.name = name
#         self.surname = surname
#
#     def print_info(self):
#         return self.name, self.surname, self.id
#
# class Book:
#     def __init__(self, id, name, author):
#         self.id = id
#         self.name = name
#         if isinstance(author, Author):
#             self.author = author
#         else:
#             self.author = None
#             print("Invalid")
#         self.is_borrowing = False
#
#     def print_info(self):
#         return self.id, self.name, self.author.print_info() if self.author is None else self.author.print_info()
#
#
# class Student:
#     def __init__(self,id,fullname):
#         self.id = id
#         self.fullname = fullname
#         self.list_of_book = list()
#
#     def add_book(self, book):
#         if isinstance(book, Book):
#             if book.is_borrowing == False
#                 if len(self.borrow_book_list) < 3:
#                     self.borrow_book_list.append(book)
#                 else:
#                     print("Length of the list exceeds the 3!")
#
