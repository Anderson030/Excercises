books = []

def add_book():
    title = input("Enter TITLE: ").strip()
    author = input("Enter AUTHOR: ").strip()
    stock = int(input("Enter the amount: "))
    books.append({"title": title, "author": author, "stock": stock})
    print("Book added successfully.\n")

def find_book():
    search = input("Enter title to search: ").strip().lower()
    for book in books:
        if search in book["title"].lower():
            print(f"Found: {book}")
            return
    print("Book not found.\n")

def show_books():
    if not books:
        print("No books.\n")
    for book in books:
        print(book)

# Example menu
def menu():
    while True:
        print("1. Add book")
        print("2. Find book")
        print("3. Show all books")
        print("4. Exit")
        option = input("Select an option: ").strip()
        if option == "1":
            add_book()
        elif option == "2":
            find_book()
        elif option == "3":
            show_books()
        elif option == "4":
            break
        else:
            print("Option no valid.\n")

menu()