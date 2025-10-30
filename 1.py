from datetime import datetime, timedelta

# -------------------- BOOK CLASS --------------------

# Book class -  har ek kitab ka details rakhta hai
class Book:
    def __init__(self, book_title, book_author, publish_year, available_copies): 
        # Book ke basic details
        self.title = book_title
        self.author = book_author
        self.year = publish_year
        self.total_copies = available_copies  
        self.available_copies = available_copies  # Kitni copies available hai
        self.issued = []   # Issued books ka record - kis student ne kab issue kiya

    # Book ki information ek string me return hoti hai
    def get_info(self):
        if self.available_copies > 0:
            status = "Available"
        else:
            status = "Out Of Stock! Choose Another Book!"
    
        return f"{self.title} by {self.author} || ({self.year}) " \
                f"Available : {self.available_copies}/{self.total_copies} | {status}"


# -------------------- LIBRARY CLASS --------------------

# Library class me sari books manage hoti hain
class Library:
    def __init__(self):
        self.books = []   #  List - jisme sari books store hoti hain


    # ---------- ADD BOOK -------------
    # Nayi book add karna
    def add_book(self, title, author, year, copies):
        book = Book(title, author, year, copies)   # Book --> object banaya 
        self.books.append(book)  # Book  - ko library me add kiya hai
        print(f"Book '{title}' Added Successfully !!!! ")

    # ------------ VIEW BOOK ---------------
    # Sari available books view hoti hai
    def view_books(self):
        if len(self.books) == 0:
            print("No Books Available In The Library!")
        else:
            print('\n'  + '-' * 5 + " Library Books "  + '-' * 5 )
            i = 1   # Book - allways start with 1 
            for book in self.books:
                print(f"{i}. {book.get_info()}")  # Har book ka info print karta hai
                i += 1   

    # ------------ UPDATE BOOK ---------------
    # Book details - title, author, year - update karta hai
    def update_book(self, index, title, author, year):
        try:
            book = self.books[index]
            book.title = title
            book.author = author
            book.year = year
            print("Book updated successfully!")

        except IndexError:
            print("Invalid Book Number! Enter Valid Book Number")

    # ------------ DELETE BOOK ---------------
    # Book -- delete karta hai --  library se
    def remove_book(self, index):
        try:
            removed_book = self.books.pop(index)
            print(f"Book '{removed_book.title}' deleted successfully!")
        except IndexError:
            print("Invalid Book ! Cannot delete ! Enter Valid Number." )

    # ------------ ISSUE BOOK ---------------
    # Student ko book issue karta hai -  7 days ke liye
    def issue_book(self, index, student):
        try:
            book = self.books[index]   

            if book.available_copies > 0:
                issue_date = datetime.now().date()   # Issue ka date
                return_date = issue_date + timedelta(days=7)   # Return date = 7 din baad

                # Record maintain hota hai -  student ne issue kiya ki nhi to
                record = {
                    "student": student,
                    "issue_date": issue_date,
                    "return_date": return_date
                }

                book.issued.append(record)     # Record book me add karta hai
                book.available_copies -= 1      # Copies kam karta hai

                print(f"'{book.title}' issued to {student}. Return by {return_date}.")
            else:
                print("Sorry, No Copies Available.")

        except IndexError:
            print("Chose Valid Option !")       

    # ------------ RETURN BOOK ---------------
    # Student ne jo book issue ki thi, usko return karta hai
    def return_book(self, index, student):
        try:
            book = self.books[index]   
    
            for record in book.issued:
                if record["student"] == student:
                    book.issued.remove(record)      # Record remove kiya jaata hai
                    book.available_copies += 1      # Copy wapas add hoti hai
                    print(f"'{book.title}' returned by {student}. Thanks!")
                    return
    
            print("This Student Has Not Issued This Book.")  # Agar record nahi mila to This line print
    
        except IndexError:
            print("Invalid book number! Enter Valid Number") # Invalide option dala to - str / special charetor


# -------------------- STUDENT MENU --------------------
# Yeh menu students ke liye hai
def student_menu(library):
    while True:
        print("\n"  + '-' * 5 + " Student Menu "  + '-' * 5 )
        print("1. View Books")       # Sari books Dikhat hai
        print("2. Issue Book")       # Book issue karta hai
        print("3. Return Book")      # Book return karta hai
        print("4. Exit")             # Exit 

        choice = input("\nEnter Your Choice : ")

        if choice == "1":
            print("\nAvailable Books:")
            library.view_books()   # Library class ke view_books() function ko call hota hai ---> imp

        elif choice == "2":
            print("\nIssue a Book")
            library.view_books()   # Books list dikhata hai
            try:
                index = int(input("Enter book number to issue: ")) - 1
                student = input("Enter your name: ")
                library.issue_book(index, student)   # Library class ke issue_book() function call hota hai
            except ValueError:
                print("Please enter a valid number!")

        elif choice == "3":
            print("\nReturn a Book")
            library.view_books()
            try:
                index = int(input("Enter book number to return: ")) - 1
                student = input("Enter your name: ")
                library.return_book(index, student)   # Library class ke return_book() function call hot ahe
            except ValueError:
                print("Please Enter a Valid Number!")

        elif choice == "4":
            print("Back to Main Menu...")
            break

        else:
            print("Invalid Option ! Enter valid Option.")


# -------------------- OWNER MENU --------------------
# Yeh menu library owner ke liye hai
def owner_menu(library):
    while True:
        print("\n"  + '-' * 5 + " Owner Menu "  + '-' * 5 )
        print("1. Add Book")          # Book add karta hai
        print("2. Update Book")       # Book update karta hai
        print("3. Remove Book")       # Book remove karta hai
        print("4. View Books")        # Books dikhata hai
        print("5. Back to Main Menu") # Exit

        choice = input("\nEnter your choice : ")

        if choice == "1":
            print("\nAdd a New Book")
            title = input("Enter title: ")
            author = input("Enter author: ")
            year = input("Enter year: ")
            copies = int(input("Enter number of copies: "))
            library.add_book(title, author, year, copies)   # Library class ke add_book() function call hot hai.

        elif choice == "2":
            print("\nUpdate Book Details")
            library.view_books()
            try:
                index = int(input("Enter book number to update: ")) - 1
                title = input("Enter new title: ")
                author = input("Enter new author: ")
                year = input("Enter new year: ")
                library.update_book(index, title, author, year)  # Library class ke update_book() function call hot ahe.
            except ValueError:
                print("Please enter a valid number!")

        elif choice == "3":
            print("\nRemove a Book")
            library.view_books()
            try:
                index = int(input("Enter Book Number To Remove: ")) - 1
                library.remove_book(index)   # Library class ke remove_book() function call hot hai
            except ValueError:
                print("Please Enter a Valid Number !")

        elif choice == "4":
            print("\nLibrary Books List")
            library.view_books()   # Library class ke view_books() function call hotahai.

        elif choice == "5":
            print("Back to Main Menu...")
            break

        else:
            print("Invalid choice! Enter Valid Choice.")


# -------------------- MAIN MENU --------------------
# Yeh system ka starting point hai -->>> read carefully
def main_menu(library):
    while True:
        print("\n" + '-' * 5 + " Welcome to Library Management System "  + '-' * 5 )
        print("1. Student")   # Student ke liye menu
        print("2. Owner")     # Owner ke liye menu
        print("3. Exit")      # Program exit

        choice = input("\nEnter your choice (1-3): ")

        if choice == "1":
            student_menu(library)   # Student menu call -->>> or class Calll

        elif choice == "2":
            owner_menu(library)     # Owner menu call ----->>> or class call

        elif choice == "3":
            print("\n Goodbye! Have Nice Day")
            break

        else:
            print("Invalid Option! Please Enter Valid Option !!!")


# -------------------- STARTING POINT --------------------
if __name__ == "__main__":  # ------>>>>>>>>>>>>>>>>   name - variable hai - main ka 
    lib = Library()  ### ----------------->>>>>>>>>>>> lib - object hai - library class ka

    ###########------------------>>>>>>>>>>>>>..  Agara - __name__ == "__main__" - hai To --->> to hi run hoga nhi to Error

    # Pre-added books in library (Library class ke add_book() function call)
    
    lib.add_book("The Great Gatsby", "F. Scott Fitzgerald", 1925, 3)
    lib.add_book("To Kill a Mockingbird", "Harper Lee", 1960, 5)
    lib.add_book("1984", "George Orwell", 1949, 4)
    lib.add_book("Pride and Prejudice", "Jane Austen", 1813, 6)
    lib.add_book("The Catcher in the Rye", "J.D. Salinger", 1951, 2)
    lib.add_book("The Hobbit", "J.R.R. Tolkien", 1937, 7)
    lib.add_book("Moby Dick", "Herman Melville", 1851, 3)
    lib.add_book("War and Peace", "Leo Tolstoy", 1869, 2)
    lib.add_book("The Odyssey", "Homer", -700, 4)
    lib.add_book("Harry Potter and the Sorcerer’s Stone", "J.K. Rowling", 1997, 10)

     # Run main menu
    main_menu(lib) ###------->>>>>>>>>. ye sare func show karta hai lib ke andar ke



###### Abhi koi demand nhi karega Kuch raha to bus puch lena call karke Good Night ! 
# Isase bus sumjo Commet se without comment alg hai
