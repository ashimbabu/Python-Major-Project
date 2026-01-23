import json
import os

FILE_NAME = "library.json"

# ---------- File Handling ----------
def load_books():
    if not os.path.exists(FILE_NAME):
        return {}
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_books(books):
    with open(FILE_NAME, "w") as file:
        json.dump(books, file, indent=4)

# ---------- Core Functions ----------
def add_book():
    books = load_books()
    book_id = input("Enter Book ID: ")

    if book_id in books:
        print("Book ID already exists!")
        return

    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    quantity = int(input("Enter Quantity: "))

    books[book_id] = {
        "Title": title,
        "Author": author,
        "Quantity": quantity
    }

    save_books(books)
    print("Book added successfully!")

def view_books():
    books = load_books()
    if not books:
        print("No books available.")
        return

    print("\n--- Library Books ---")
    for bid, details in books.items():
        print(f"\nBook ID: {bid}")
        for key, value in details.items():
            print(f"{key}: {value}")

def search_book():
    books = load_books()
    keyword = input("Enter Book ID or Title: ").lower()

    found = False
    for bid, details in books.items():
        if keyword == bid.lower() or keyword in details["Title"].lower():
            print(f"\nBook ID: {bid}")
            for k, v in details.items():
                print(f"{k}: {v}")
            found = True

    if not found:
        print("Book not found!")

def issue_book():
    books = load_books()
    book_id = input("Enter Book ID to issue: ")

    if book_id in books:
        if books[book_id]["Quantity"] > 0:
            books[book_id]["Quantity"] -= 1
            save_books(books)
            print("Book issued successfully!")
        else:
            print("Book out of stock!")
    else:
        print("Book not found!")

def return_book():
    books = load_books()
    book_id = input("Enter Book ID to return: ")

    if book_id in books:
        books[book_id]["Quantity"] += 1
        save_books(books)
        print("Book returned successfully!")
    else:
        print("Book not found!")

def delete_book():
    books = load_books()
    book_id = input("Enter Book ID to delete: ")

    if book_id in books:
        del books[book_id]
        save_books(books)
        print("Book deleted successfully!")
    else:
        print("Book not found!")

# ---------- Main Menu ----------
def main():
    while True:
        print("\n===== Library Management System =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Delete Book")
        print("7. Exit")

        choice = input("Enter choice (1-7): ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            issue_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            delete_book()
        elif choice == "7":
            print("Thank you for using Library Management System.")
            break
        else:
            print("Invalid choice! Try again.")

# ---------- Run Program ----------
if __name__ == "__main__":
    main()
