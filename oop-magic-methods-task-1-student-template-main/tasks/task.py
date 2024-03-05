from typing import List


class Counter:
    def __init__(self, values: List[int]):
        self.values = values
    
    def __add__(self, b):
        if isinstance(b, str):
            return [f"{num} {b}" for num in self.values]
        else:
            raise TypeError("Unsupported operand type(s) for +: 'Counter' and '{}'".format(type(b).__name__))
        

print(Counter([1, 2, 3]) + "mississippi")