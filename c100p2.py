class Book(object):
    def _init_(self,name,pages,price):
        self.name=name
        self.pages=pages
        self.price=price

    def start(self):
        print("Books")
    def bookpages(self,pages):
        print("Number of pages in book : "+pages)


harrypotter = Book("harrypotter", 39)

print(harrypotter.bookpages())