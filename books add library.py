#Create Library
class Library:
    def __init__(self):
        self.book= []
        
    def add_books(self, title, author, copies):
        add_ = []
        add_.append(title)
        add_.append(author)
        add_.append(copies)
        self.book.append(add_)
        
    def display_books(self):
        for i in self.book:
            print("Title: {}, Author: {}, Copies: {}".format(i[0], i[1], i[2]))
        #print("Title: {}, Author: {}, Copies: {}".format(self.title, self.author, self.copies))
    
    def search_for_book(self, title):
            for i in self.book:
                if (i[0] == "Title"):
                    print(i)


bo = Library()
bo.add_books("Blue", "ali", 5)
bo.add_books("Red", "Ahmed", 7)
bo.display_books()
bo.search_for_book("Blue")
