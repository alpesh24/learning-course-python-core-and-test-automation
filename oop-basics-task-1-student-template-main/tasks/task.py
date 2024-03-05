class Field:
    __value = None
    def __init__(self):
        self.__value = None
    
    def get_value(self):
        return self.__value
    
    def set_value(self, v):
        self.__value = v

obj = Field()
obj.set_value(100)
print(obj.get_value())

