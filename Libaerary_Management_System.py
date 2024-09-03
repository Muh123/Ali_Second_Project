<<<<<<< HEAD
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

class User:
    def __init__(self, username):
        self.username = username
        self.borrowed_books = []

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f'Book "{title}" by {author} added to the library.')

    def register_user(self, username):
        new_user = User(username)
        self.users.append(new_user)
        print(f'User "{username}" registered successfully.')

    def view_books(self):
        if not self.books:
            print("No books available in the library.")
            return
        for book in self.books:
            status = "Borrowed" if book.is_borrowed else "Available"
            print(f'Title: "{book.title}", Author: {book.author}, Status: {status}')

    def borrow_book(self, username, title):
        user = self.find_user(username)
        if not user:
            print(f'User "{username}" not found.')
            return
        
        for book in self.books:
            if book.title == title and not book.is_borrowed:
                book.is_borrowed = True
                user.borrowed_books.append(book)
                print(f'User "{username}" has borrowed "{title}".')
                return
        print(f'Sorry, "{title}" is not available.')

    def return_book(self, username, title):
        user = self.find_user(username)
        if not user:
            print(f'User "{username}" not found.')
            return
        
        for book in user.borrowed_books:
            if book.title == title:
                book.is_borrowed = False
                user.borrowed_books.remove(book)
                print(f'User "{username}" has returned "{title}".')
                return
        print(f'User "{username}" did not borrow "{title}".')

    def find_user(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None

    def search_books(self, query):
        found_books = [book for book in self.books if query.lower() in book.title.lower()]
        if found_books:
            for book in found_books:
                status = "Borrowed" if book.is_borrowed else "Available"
                print(f'Found - Title: "{book.title}", Author: {book.author}, Status: {status}')
        else:
            print(f'No books found matching "{query}".')

# Main Program
if __name__ == "__main__":
    library = Library()

    # Sample Data
    library.add_book("The Great Gatsby", "F. Scott Fitzgerald")
    library.add_book("To Kill a Mockingbird", "Harper Lee")
    library.add_book("1984", "George Orwell")

    # User Registration
    library.register_user("Ali")
    library.register_user("Hamza")

    # Viewing Books
    print("\nAvailable Books:")
    library.view_books()

    # Borrowing Books
    library.borrow_book("alice", "1984")
    library.borrow_book("bob", "The Great Gatsby")

    # Viewing Books after borrowing
    print("\nBooks After Borrowing:")
    library.view_books()

    # Returning Books
    library.return_book("alice", "1984")

    # Final State of Books
    print("\nFinal State of Books:")
    library.view_books()

    # Search for a Book
    print("\nSearch Results:")
    library.search_books("Great")
=======
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

class User:
    def __init__(self, username):
        self.username = username
        self.borrowed_books = []

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f'Book "{title}" by {author} added to the library.')

    def register_user(self, username):
        new_user = User(username)
        self.users.append(new_user)
        print(f'User "{username}" registered successfully.')

    def view_books(self):
        if not self.books:
            print("No books available in the library.")
            return
        for book in self.books:
            status = "Borrowed" if book.is_borrowed else "Available"
            print(f'Title: "{book.title}", Author: {book.author}, Status: {status}')

    def borrow_book(self, username, title):
        user = self.find_user(username)
        if not user:
            print(f'User "{username}" not found.')
            return
        
        for book in self.books:
            if book.title == title and not book.is_borrowed:
                book.is_borrowed = True
                user.borrowed_books.append(book)
                print(f'User "{username}" has borrowed "{title}".')
                return
        print(f'Sorry, "{title}" is not available.')

    def return_book(self, username, title):
        user = self.find_user(username)
        if not user:
            print(f'User "{username}" not found.')
            return
        
        for book in user.borrowed_books:
            if book.title == title:
                book.is_borrowed = False
                user.borrowed_books.remove(book)
                print(f'User "{username}" has returned "{title}".')
                return
        print(f'User "{username}" did not borrow "{title}".')

    def find_user(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None

    def search_books(self, query):
        found_books = [book for book in self.books if query.lower() in book.title.lower()]
        if found_books:
            for book in found_books:
                status = "Borrowed" if book.is_borrowed else "Available"
                print(f'Found - Title: "{book.title}", Author: {book.author}, Status: {status}')
        else:
            print(f'No books found matching "{query}".')

# Main Program
if __name__ == "__main__":
    library = Library()

    # Sample Data
    library.add_book("The Great Gatsby", "F. Scott Fitzgerald")
    library.add_book("To Kill a Mockingbird", "Harper Lee")
    library.add_book("1984", "George Orwell")

    # User Registration
    library.register_user("Ali")
    library.register_user("Hamza")

    # Viewing Books
    print("\nAvailable Books:")
    library.view_books()

    # Borrowing Books
    library.borrow_book("alice", "1984")
    library.borrow_book("bob", "The Great Gatsby")

    # Viewing Books after borrowing
    print("\nBooks After Borrowing:")
    library.view_books()

    # Returning Books
    library.return_book("alice", "1984")

    # Final State of Books
    print("\nFinal State of Books:")
    library.view_books()

    # Search for a Book
    print("\nSearch Results:")
    library.search_books("Great")
>>>>>>> f8859e26249d598fc0ab8e3df935087c9829ef05
