class PriceControl:
    """
    Descriptor which don't allow to set price
    less than 0 and more than 100 included.
    """
    def __init__(self, initial_price=0) -> None:
        self._price = initial_price

    def __get__(self, instance, owner):
        return self._price
    
    def __set__(self, instance, value):
        try:
            if not (0 <= value <= 100) or (value is None):
                raise ValueError("ValueError: Price must be between 0 and 100.")
            else:
                self._price = value
        except ValueError as ve:
            print(ve)
        
        

class NameControl:
    """
    Descriptor which don't allow to change field value after initialization.
    """
    def __init__(self, initial_value) -> None:
        self._value = initial_value

    def __get__(self, instance, owner):
        return self._value
    
    def __set__(self, instance, value):
        try:
            if hasattr(instance, '_initialized') and instance._initialized:
                raise ValueError(f"ValueError: Name can not be changed.")
            else:
                self._value = value
        except ValueError as ve:
            print(ve)



class Book:
    author = NameControl("")
    name = NameControl("")
    price = PriceControl()

    def __init__(self, author, name, price) -> None:
        self.price = price
        self.author = author
        self.name = name
        self._initialized = True

    def __repr__(self):
        return f"Book(author='{self.author}', name='{self.name}', price={self.price})"

b = Book("William Faulkner", "The Sound and the Fury", 12)
print(f"Author='{b.author}', Name='{b.name}', Price='{b.price}'")

b.price = 55
print(b.price)

b.price = -1
b.price = 102

b.author = "William Shakeoseare"
#print(b.author)
b.name = "Hamlet"
#print(b.name)