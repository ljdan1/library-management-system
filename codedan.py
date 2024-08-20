import os

class Library:
    def __init__(self):
        self.books = []
        self.logged_in_user = None
    
    def add_book(self):
        name = input("Enter the book name you want to add: ")
        author_name = input("Enter the author name: ")
        book_id = int(input("Enter the ID of the book: "))
        shelf = input("Enter the position of the book on the shelf: ")
        status = input("Enter the status (borrowed or in library): ")
        book = {"name": name, "author_name": author_name, "book_id": book_id, "shelf": shelf, "status": status}
        self.books.append(book)
        print("You have successfully added the book.")

    def display_books(self):
        if len(self.books) < 1:
            print("No books in the library.")
        else:
            print("The books in the library are:")
            for book in self.books:
                print(book)

    def search_book(self):
        book_id = int(input("Enter the ID of the book you want to search for: "))
        found = False
        for book in self.books:
            if book["book_id"] == book_id:
                print("Yes, the book is in the library.")
                found = True
                break
        if not found:
            print("Sorry, the book is not in the library.")

    def edit_book(self):
        book_id = int(input("Enter the book ID you want to edit: "))
        for book in self.books:
            if book["book_id"] == book_id:
                status = input("Enter the new status: ")
                shelf = input("Enter the new position of the book: ")
                book["shelf"] = shelf
                book["status"] = status
                print("Your edit is successful.")
                print("The new book's data is", book)
                return
        print("Book not found.")

    def remove_book(self):
        book_id = int(input("Enter the book ID you want to remove: "))
        for book in self.books:
            if book["book_id"] == book_id:
                self.books.remove(book)
                print("Successfully removed.")
                print("The other books in the library are", self.books)
                return
        print("Book not found.")

    def librarian_login(self):
        username = input("Enter librarian username: ")
        password = input("Enter librarian password: ")
        # Simple check for demonstration purposes
        if username == "librarian" and password == "password":
            self.logged_in_user = "librarian"
            print("Librarian logged in successfully.")
            self.librarian_menu()
        else:
            print("Invalid credentials. Please try again.")
    
    def student_login(self):
        self.logged_in_user = "student"
        print("Student logged in successfully.")
        self.student_menu()

    def librarian_menu(self):
        while True:
            print("*** LIBRARIAN MENU ***")
            print("1. Add a book")
            print("2. Display books")
            print("3. Edit book details")
            print("4. Remove a book")
            print("0. Logout")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                self.add_book()
            elif choice == 2:
                self.display_books()
            elif choice == 3:
                self.edit_book()
            elif choice == 4:
                self.remove_book()
            elif choice == 0:
                print("Logging out...")
                self.logged_in_user = None
                break
            else:
                print("You entered a wrong number. Please try again.")
            input("Press Enter to continue...")  # Adding pause before clearing the screen again
            os.system("cls" if os.name == "nt" else "clear")  # Clearing the screen
    
    def student_menu(self):
        while True:
            print("*** STUDENT MENU ***")
            print("1. Display books")
            print("2. Search for a book")
            print("0. Logout")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                self.display_books()
            elif choice == 2:
                self.search_book()
            elif choice == 0:
                print("Logging out...")
                self.logged_in_user = None
                break
            else:
                print("You entered a wrong number. Please try again.")
            input("Press Enter to continue...")  # Adding pause before clearing the screen again
            os.system("cls" if os.name == "nt" else "clear")  # Clearing the screen

def main():
    library = Library()
    while True:
        print("-----------------------------------------------------------------------------")
        print("                *** Welcome to our library ***")
        print("-----------------------------------------------------------------------------")
        print("1. Librarian Login")
        print("2. Student Login")
        print("0. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            library.librarian_login()
        elif choice == 2:
            library.student_login()
        elif choice == 0:
            print("You have finished. Thank you. Goodbye!")
            break
        else:
            print("You entered a wrong number. Please try again.")
        input("Press Enter to continue...")  # Adding pause before clearing the screen again
        os.system("cls" if os.name == "nt" else "clear")  # Clearing the screen

if __name__ == "__main__":
    main()
