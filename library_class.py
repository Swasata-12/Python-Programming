# Write a library class with no of books and books as two instance variables. Write a program to create a 
# library from this Library class and show how you can print all books, add a book and get the number of books 
# using different methods. Show that your program does not persists the books after the program is stopped.

class Library:
    def __init__(self):
        self.noBooks=0
        self.books=[]


    def addBook(self,book):
        self.books.append(book)
        self.noBooks=len(self.books)


    def showInfo(self):
        print(f"The Library has {self.noBooks} books and they are:")
        for item in self.books:
            print(item)


l1=Library()
l1.addBook("Harry Potter")
l1.addBook("Python for Begginers")
l1.addBook("Superman Returns")
l1.showInfo()