class Book:
    """Класс, представляющий книгу
    """

    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre


    def __repr__(self):
       return 'Book({!r}, {!r}, {!r})'.format(self.title, self.year, self.genre)


    def __str__(self):
        return 'Book({!r}, {!r}, {!r})'.format(self.title, self.year, self.genre)


book1 = Book("War and peace", 1869, "novel")
book2 = Book("Lord of the rings", 1954, "fantasy")
print(book1)
print(book2)
# Задание: создайте несколько объектов класса Book
# и выведите их на экран
