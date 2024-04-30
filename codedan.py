import os

user = []

def add_book():
    name = input("Enter the book name you want to add: ")
    outer_name = input("Enter the author name: ")
    book_id = int(input("Enter the ID of the book: "))
    shelf = input("Enter the position of the book on the shelf: ")
    status = input("Enter the status (borrowed or in library): ")
    users = {"name": name, "outer_name": outer_name, "book_id": book_id, "shelf": shelf, "status": status}
    user.append(users)
    print("You have successfully added the book.")

def display():
    if len(user) < 1:
        print("No books in the library.")
    else:
        print("The books in the library are:")
        for book in user:
            print(book)

def search():
    ch = int(input("Enter the ID of the book you want to search for: "))
    found = False
    for i in user:
        if i["book_id"] == ch:
            print("Yes, the book is in the library.")
            found = True
            break
    if not found:
        print("Sorry, the book is not in the library.")

def edit():
    x = int(input("Enter the book ID you want to edit: "))
    for i in user:
        if i["book_id"] == x:
            s = input("Enter the new status: ")
            sh = input("Enter the new position of the book: ")
            i["shelf"] = sh
            i["status"] = s
            print("Your edit is successful.")
            print("The new book's data is", user)
            return
    print("Book not found.")

def remove():
    x = int(input("Enter the book ID you want to remove: "))
    for i in user:
        if i["book_id"] == x:
            user.remove(i)
            print("Successfully removed.")
            print("The other books in the library are", user)
            return
    print("Book not found.")

print("-----------------------------------------------------------------------------")
print("                *** Welcome to our library ***")
print("-----------------------------------------------------------------------------")
print("     Our library rules are:")
print("1. You can edit only the book's status and position.")
print("2. You can use each book for only 1 hour.")
print(".............................................................................")
while True:
   
    print("*** MENU ***")
    print("1. Add a book")
    print("2. Display books")
    print("3. Search for a book")
    print("4. Edit book details")
    print("5. Remove a book")
    print("0. Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        add_book()
    elif ch == 2:
        display()
    elif ch == 3:
        search()
    elif ch == 4:
        edit()
    elif ch == 5:
        remove()
    elif ch == 0:
        print("You have finished. Thank you. Goodbye!")
        break
    else:
        print("You entered a wrong number. Please try again.")
    input("Press Enter to continue...")  # Adding pause before clearing the screen again
    os.system("cls" if os.name == "nt" else "clear")  # Clearing the screen
