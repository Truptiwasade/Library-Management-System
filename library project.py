from datetime import datetime

# Library Book List
library = []

# Add a book
def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    year = input("Enter publication year: ")
    try:
        copies = int(input("Enter number of copies: "))
    except ValueError:
        print("Invalid input. Number of copies must be a number.")
        return

    status = "Available" if copies > 0 else "Out of Stock"
    library.append({
        "title": title,
        "author": author,
        "year": year,
        "copies": copies,
        "issue_date": "",
        "return_date": "",
        "status": status
    })
    print("Book added successfully!")

# Display all books
def display_books():
    if not library:
        print("No books in the library.")
        return
    print("\nLibrary Collection:")
    for book in library:
        print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, "
              f"Copies: {book['copies']}, Status: {book['status']}, "
              f"Issue Date: {book['issue_date']}, Return Date: {book['return_date']}")

# Search for a book
def search_book():
    title = int(input("Enter book no. to search: "))
    for book in library:
        if book["title"].lower() == title.lower():
            print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, "
                  f"Copies: {book['copies']}, Status: {book['status']}, "
                  f"Issue Date: {book['issue_date']}, Return Date: {book['return_date']}")
            return
    print("Book not found.")

# Delete a book
def delete_book():
    title = input("Enter book no. to delete: ")
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print("Book deleted successfully.")
            return
    print("Book not found.")

from datetime import datetime, timedelta

# Issue book
def issue_book():
    title = input("Enter title of the book to issue: ")
    for book in library:
        if book["title"].lower() == title.lower():
            if book["copies"] > 0:
                book["copies"] -= 1
                book["issue_date"] = datetime.now().strftime("%Y-%m-%d")
                
                # Auto set return date to 7 days later
                book["return_date"] = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")
                
                book["status"] = "Available" if book["copies"] > 0 else "Out of Stock"
                print(f"Book '{book['title']}' issued successfully.")
                print(f"Issue Date: {book['issue_date']}")
                print(f"Return By: {book['return_date']}")
            else:
                print("Book is currently out of stock.")
            return
    print("Book not found.")

# Return book
def return_book():
    title = input("Enter title of the book to return: ")
    for book in library:
        if book["title"].lower() == title.lower():
            if book["copies"] >= 0:
                try:
                    expected_return_date = datetime.strptime(book["return_date"], "%Y-%m-%d")
                    actual_return_date = datetime.now()
                    late_days = (actual_return_date - expected_return_date).days

                    if late_days > 0:
                        fine = late_days * 10
                        print(f"Returned late by {late_days} day(s). Fine: ₹{fine}")
                    else:
                        print("Book returned on time. No fine.")

                except ValueError:
                    print("Invalid date format in return record.")
                    return

                book["copies"] += 1
                book["issue_date"] = ""
                book["return_date"] = ""
                book["status"] = "Available"
                print(f"Book '{book['title']}' returned successfully.")
                return
    print("Book not found.")


# Main Menu
def main():
    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Search Book")
        print("4. Delete Book")
        print("5. Issue Book")
        print("6. Return Book")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            display_books()
        elif choice == '3':
            search_book()
        elif choice == '4':
            delete_book()
        elif choice == '5':
            issue_book()
        elif choice == '6':
            return_book()
        elif choice == '7':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# Run the program
main()
