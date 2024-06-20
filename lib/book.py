#!/usr/bin/env python3

class Book:
    def __init__(self, title):
        self.title = title

    def get_page_count(self):
        try:
            return self._page_count
        except:
            return
    
    def set_page_count(self, page_count):
        if (type(page_count) == int):
            self._page_count = page_count
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
    
    page_count = property(get_page_count, set_page_count)

# Book in book.py gets initialized with a title.
# Book in book.py has the title passed into __init__.
# Book in book.py can be assigned an author name.
# Book in book.py can be assigned a page count property.
# Book in book.py prints "page_count must be an integer" if page_count is not an integer.
# Book in book.py can be assigned a genre.
# Book in book.py outputs "Flipping the page...wow, you read fast!" when method turn_page() is called