class Library:
    def __init__(self, list_of_books, library_name):
        self.library_name = library_name
        self.list_of_books = list_of_books

    def display_books(self):
        print(f"Library name is {self.library_name}")
        print(f"Here is the list of books we provide:{self.list_of_books}")

    def add_book(self):
        print("Name of book?")
        book = input().capitalize()
        self.list_of_books.append(book)
        print("Awesome! Here we have a new source of knowledge")
        print(self.list_of_books)

    def lend_book(self):
        print("Enter your name:")
        name = input()
        # d1 = {}
        print("Which book you want to lend?")
        book = input().lower()
        if book in self.list_of_books:
            print(f"Now {name} is the owner of book: {book}")
            self.list_of_books.remove(book)
        else:
            print("Currently not available")

    def return_book(self):
        print("Name of the book you want to return")
        ham = input()
        print("Hope you enjoyed reading!")
        self.list_of_books.append(ham)


lst = ["hi", "bi", "mi", "vi"]
obj = Library(lst, "Read_Me")

if __name__ == '__main__':
    while True:
        print("Enter your requirements Sir/Mam: 1.Show Books[show]  "
              "2.Lend Books[lend]  "
              "3.Add Book[add]  "
              "4.Return Book[return]"
              )
        need = input().upper()
        if need == "SHOW":
            obj.display_books()
        elif need == "LEND":
            obj.lend_book()
        elif need == "ADD":
            obj.add_book()
        else:
            obj.return_book()
