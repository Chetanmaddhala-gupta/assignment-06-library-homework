class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        status = "borrowed" if self.is_borrowed else "available"
        return f"{self.title} by {self.author} ({status})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book(self, title):
        return next((book for book in self.books if book.title.casefold() == title.casefold()), None)

    def borrow(self, title):
        book = self.find_book(title)
        if book is None or book.is_borrowed:
            return False
        book.is_borrowed = True
        return True

    def return_book(self, title):
        book = self.find_book(title)
        if book is None or not book.is_borrowed:
            return False
        book.is_borrowed = False
        return True


def main():
    library = Library()
    library.add_book(Book("The Hobbit", "J. R. R. Tolkien"))
    library.add_book(Book("Pride and Prejudice", "Jane Austen"))
    while True:
        print("\n1. List books  2. Add book  3. Borrow  4. Return  5. Quit")
        choice = input("Choose: ").strip()
        if choice == "1":
            for book in library.books:
                print("-", book)
        elif choice == "2":
            library.add_book(Book(input("Title: ").strip(), input("Author: ").strip()))
            print("Book added.")
        elif choice in {"3", "4"}:
            title = input("Book title: ").strip()
            success = library.borrow(title) if choice == "3" else library.return_book(title)
            print("Done." if success else "Book not found or its status does not allow that action.")
        elif choice == "5":
            break
        else:
            print("Please choose 1–5.")


if __name__ == "__main__":
    main()
