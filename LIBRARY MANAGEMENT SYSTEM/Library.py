class Library:
    def __init__(self):
        self.books = []

    def add_books(self, title, author, copies):
        book = {"title": title, "author": author, "copies": copies}
        # book = Book(title, author, copies)
        self.books.append(book)
        print(f'Book "{title}" by {author} added with {copies} copies.')

    def display_info(self):
        if len(self.books) == 0:
            print("No books in the library.")
        else:
            print("There are books present in library")
            for book in self.books:
                print(
                    f"Title: {book['title']}, Author:{book['author']}, Copies:{book['copies']}"
                )

    def borrow_books(self, title):
        for book in self.books:
            if book["title"] == title:
                if book["copies"] > 0:
                    book["copies"] -= 1
                    print(f"book borrowed of title '{title}'")
                else:
                    print(f"No copies of book of title '{title}' available")
                return
        print(f"books of title '{title}' is not available ")

    def return_books(self, title):
        for book in self.books:
            if book["title"] == title:
                book["copies"] += 1
                print(f"thankyou for returning book of Title: {title}")
                return


library = Library()
while True:
    print("1.Add books")
    print("2.Display Information")
    print("3.Borrow books")
    print("4.Return books")
    print("5.Exit")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 5.")
        continue

    if choice == 1:
        title = input("Enter the title = ")
        author = input("Enter the author = ")
        copies = int(input("Enter the total number of copies = "))
        library.add_books(title, author, copies)

    elif choice == 2:
        library.display_info()

    elif choice == 3:
        title = input("Enter the title of book you want to borrow = ")
        library.borrow_books(title)

    elif choice == 4:
        title = input("Enter the title of book you want to return = ")
        library.return_books(title)

    elif choice == 5:
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice! Please select a valid option.")
