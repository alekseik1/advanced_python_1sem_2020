class Book:
    is_printed = True

    @classmethod
    def describe(cls):
        print('type:', cls)
        if cls.is_printed:
            print('I am printed')
        else:
            print('I am not printed')
class EBook(Book):
    is_printed = False

    def __init__(self):
        self.is_printed = True


Book.describe()
EBook.describe()
EBook().describe()

