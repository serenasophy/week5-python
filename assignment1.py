class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self._author = author
        self.pages = pages

    def display(self):
        print(f"Title: {self.title}")
        print(f"Author: {self._author}")
        print(f"Pages: {self.pages}")

    def read(self):
        print(f"Reading '{self.title}' by {self._author}.")

class EBook(Book):
    def __init__(self, title, author, pages, file_size):
        super().__init__(title, author, pages)
        self.file_size = file_size

    def read(self):
        print(f"Reading eBook '{self.title}' ({self.file_size}MB).")

class AudioBook(Book):
    def __init__(self, title, author, pages, duration):
        super().__init__(title, author, pages)
        self.duration = duration

    def read(self):
        print(f"Listening to '{self.title}' for {self.duration} minutes.")

book1 = EBook("Digital Dreams", "J. Tech", 120, 5)
book2 = AudioBook("Sound of Pages", "L. Voice", 300, 90)

book1.display()
book1.read()

print()

book2.display()
book2.read()

