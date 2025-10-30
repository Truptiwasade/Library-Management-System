from datetime import datetime, timedelta

# -------------------------
# Data (Library)
# -------------------------
library = [
    {"title": "The Alchemist", "author": "Paulo Coelho", "year": "1988",
     "total_copies": 5, "available_copies": 5, "issued": []},
    {"title": "Harry Potter", "author": "J.K. Rowling", "year": "1997",
     "total_copies": 4, "available_copies": 4, "issued": []},
    {"title": "1984", "author": "George Orwell", "year": "1949",
     "total_copies": 3, "available_copies": 3, "issued": []}
]

# Common Functions
def view_books():
    if not library:
        print("No books available in the library.")
    else:
        print("\n--- Library Books ---")
        for i, book in enumerate(library, start=1):
            status = "Available" if book["available_copies"] > 0 else "Out of Stock"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) | "
                  f"Available: {book['available_copies']}/{book['total_copies']} | {status}")

# Owner Functions
def add_book():
    try:
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        year = input("Enter year of publication: ")
        copies = int(input("Enter number of copies: "))
        book = {"title": title, "author": author, "year": year,
                "total_copies": copies, "available_copies": copies, "issued": []}
        library.append(book)
        print("Book added successfully!")
    except ValueError:
        print("Number of copies must be a valid number.")

def update_book():
    view_books()
    if library:
        try:
            choice = int(input("Enter book number to update: "))
            if 1 <= choice <= len(library):
                book = library[choice-1]
                book["title"] = input("Enter new title: ")
                book["author"] = input("Enter new author: ")
                book["year"] = int(input("Enter new year: "))
                print("Book updated successfully!")
            else:
                print("Invalid book number.")
        except ValueError:
            print("Please enter a valid number.")

def delete_book():
    view_books()
    if library:
        try:
            choice = int(input("Enter book number to delete: "))
            if 1 <= choice <= len(library):
                removed = library.pop(choice-1)
                print(f"{removed['title']}' deleted successfully!")
            else:
                print("Invalid book number.")
        except ValueError:
            print("Please enter a valid number.")

# Student Functions
def issue_book():
    view_books()
    if library:
        try:
            choice = int(input("Enter book number to issue: "))
            if 1 <= choice <= len(library):
                book = library[choice-1]
                if book["available_copies"] > 0:
                    student = input("Enter your name: ")
                    issue_date = datetime.now().date()
                    return_date = issue_date + timedelta(days=7)
                    record = {"student": student, "issue_date": issue_date,
                              "return_date": return_date}
                    book["issued"].append(record)
                    book["available_copies"] -= 1
                    print(f"'{book['title']}' issued to {student}. Return by {return_date}.")
                else:
                    print("Sorry, no copies available.")
            else:
                print("Invalid book number.")
        except ValueError:
            print("Please enter a valid number.")

def return_book():
    view_books()
    if library:
        try:
            choice = int(input("Enter book number to return: "))
            if 1 <= choice <= len(library):
                book = library[choice-1]
                student = input("Enter your name: ")

                record = None
                for r in book["issued"]:
                    if r["student"].lower() == student.lower():
                        record = r
                        break

                if record:
                    today = datetime.now().date()
                    if today > record["return_date"]:
                        print("Book returned late! Fine = ₹100")
                    else:
                        print("Book returned on time. No fine.")
                    book["issued"].remove(record)
                    book["available_copies"] += 1
                    print(f"'{book['title']}' returned by {student}.")
                else:
                    print("No record found for this student.")
            else:
                print("Invalid book number.")
        except ValueError:
            print("Please enter a valid number.")

# Menus
def owner_menu():
    while True:
        print("\n--- Owner Menu ---")
        print("1. View Books")
        print("2. Add Book")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            view_books()
        elif choice == "2":
            add_book()
        elif choice == "3":
            update_book()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            break
        else:
            print("Invalid choice! Please enter 1-5.")

def student_menu():
    while True:
        print("\n--- Student Menu ---")
        print("1. View Books")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            view_books()
        elif choice == "2":
            issue_book()
        elif choice == "3":
            return_book()
        elif choice == "4":
            break
        else:
            print("Invalid choice! Please enter 1-4.")

# Main Program
def main():
    while True:
        print("\nLibrary Management System")
        print("1. Owner Module")
        print("2. Student Module")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            owner_menu()
        elif choice == "2":
            student_menu()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1-3.")

main()