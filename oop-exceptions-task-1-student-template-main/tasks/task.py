import math


class Pagination:
    def __init__(self, data, items_on_page):
        self.data = data
        self.items_on_page = items_on_page
        self.book = {}

    @property
    def item_count(self) -> int: 
        return len(self.data)
    
    @property
    def page_count(self) -> int:
        num_pages = math.ceil(self.item_count / self.items_on_page)
        return num_pages

    @property
    def make_book(self):
        book = {}
        for i in range(0, self.page_count):
            index_s = i*self.items_on_page
            index_e = index_s + self.items_on_page
            if(i == self.page_count-1):
                book.update({i : self.data[index_s:]})
            else:
                book.update({i : self.data[index_s:index_e]})
        return book

    def count_items_on_page(self, page_number):
        book = self.make_book
        try:
            if page_number in book.keys():
                return len(book[page_number])
            else:
                raise Exception('Exception: Invalid index. Page is missing.')
        except Exception as e:
            print(e)
    
    def find_page(self, data):
        book = self.make_book
        res = []

        for p in book.items():
            print(p)
            word = p[1].replace(" ", "")
            if (word in data) or (data in word):
                res.append(p[0])
                print(res)
        
        try:
            if res:
                return res
            else:
                raise Exception(f"Exception: '{data}' is missing on the pages")
        except Exception as e:
            print(e)

    def display_page(self, page_number):
        book = self.make_book
        
        try:
            if page_number in book.keys():
                return book[page_number]
            else:
                raise Exception('Exception: Invalid index. Page is missing.')
        except Exception as e:
            print(e)    


pages = Pagination('Your beautiful text', 5)
print(pages.page_count)
print(pages.item_count)
print(pages.make_book)

print(pages.count_items_on_page(0))
print(pages.count_items_on_page(3))
print(pages.count_items_on_page(4))

#print(pages.find_page('Your'))
#print(pages.find_page('e'))
print(pages.find_page('beautiful'))
#print(pages.find_page('great'))

print(pages.display_page(0))