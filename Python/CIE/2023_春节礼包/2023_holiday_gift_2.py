
# Book class is used to store information
class Book:
    # Private title: String
    # Private price: Float
    def __init__(self, title: str, price: float):
        self.__title = title
        self.__price = price

    def getTitle(self):
        return self.__title

    def getPrice(self):
        return self.__price

    def getBookInfo(self):
        return self.__title + "-" + str(self.__price)


# Subclass of Book - Textbook
class TextBook(Book):
    # Private edition_number: Integer
    def __init__(self, title, price, edition_number: int):
        super().__init__(title, price)
        self.__edition_number = edition_number

    def getBookInfo(self):
        return self.getTitle() + "-" + str(self.getPrice()) + "-" + str(self.__edition_number)

    def getEdition(self):
        return self.__edition_number

    def cabSubstituteFor(self, given_book):
        if given_book.getTitle() == self.getTitle():
            if self.getEdition() >= given_book.getEdition():
                return True
            else:
                return False
        else:
            return False


bio2015 = TextBook("Biology", 49.75, 2)
bio2019 = TextBook("Biology", 39.75, 3)
print(bio2019.getEdition())
print(bio2019.getBookInfo())
print(bio2019.cabSubstituteFor(bio2015))
print(bio2015.cabSubstituteFor(bio2019))
math = TextBook("Calculus", 45.25, 1)
print(bio2015.cabSubstituteFor(math))
