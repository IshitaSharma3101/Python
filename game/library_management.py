class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books currently present are : ")
        for book in self.books:
            print(f"  * {book}")

    def requestBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}.")
            self.books.remove(bookName)
            return True
        else:
            print("Not available at the moment.")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning the book.")


class Student:
    
    def requestBook(self):
        self.book = input("Enter the book you want to borrow : ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the book you want to return : ")
        return self.book

if __name__ == "__main__":
    centralLibrary = Library(["book1", "book2", "book3", "book4", "book5"])
    student = Student()
    # centralLibrary.displayAvailableBooks()
    while(True):
        welcomeMsg = '''---------Welcome to the library---------
        Please choose an option : 
        1. List all books
        2. Request a book
        3. Return a book
        4. Exit
        '''
        print(welcomeMsg)
        a = int(input("Enter a choice : "))
        if a == 1:
            centralLibrary.displayAvailableBooks()
        elif a == 2:
            centralLibrary.requestBook(student.requestBook())
        elif a == 3:
            centralLibrary.returnBook(student.returnBook())
        elif a == 4:
            print('Thanks')
            exit()
        else:
            print("Invalid choice...")
        