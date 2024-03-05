class Bird:
    def __init__(self, name) -> None:
        self.name = name
    
    def walk(self):
        return f"{self.name} bird can walk"
    
    def fly(self):
        return f"{self.name} bird can swim"

    def __str__(self) -> str:
        return f"{self.name} bird can walk and fly" 


class FlyingBird(Bird):
    def __init__(self, name, ration="grains") -> None:
        super().__init__(name)
        self.ration = ration

    def eat(self):
        return f"It eats mostly {self.ration}"
    
    def __str__(self) -> str:
        return f"{self.name} bird can walk and fly"


class NonFlyingBird(Bird):
    def __init__(self, name, ration="fish") -> None:
        super().__init__(name)
        self.ration = ration

    def fly(self):
        try:
            raise AttributeError(f"AttributeError: '{self.name}' object has no attribute '{self.fly.__name__}'")
        except AttributeError as ae:
            return(ae)

    def swim(self):
        return f"{self.name} bird can swim"
    
    def eat(self):
        return f"It eats mostly {self.ration}"
    
    def __str__(self) -> str:
        return f"{self.name} can walk and swim"

class SuperBird(NonFlyingBird, FlyingBird):
    def __init__(self, name, ration="fish") -> None:
        super().__init__(name, ration)

    def __str__(self) -> str:
        return f"{self.name} bird can walk, swim and fly"

b = Bird("Any")
print(b.walk())

p = NonFlyingBird("Penguin", "fish")
print(p.swim())
print(p.fly())
print(p.eat())

c = FlyingBird("Canary")
print(str(c))
print(c.eat())

s = SuperBird("Gull")
print(str(s))
print(s.eat())
