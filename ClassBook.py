class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def get_info(self):
        return self.title + " by " + self.author + ", " + str(self.pages) + " pages"
    
    def is_long(self):
        if self.pages > 300:
            return True
        else:
            return False


book1 = Book("Python Basics", "John Smith", 250)
book2 = Book("Advanced Python", "Jane Doe", 450)


print(book1.get_info())
print("Is long?", book1.is_long())

print(book2.get_info())
print("Is long?", book2.is_long())
