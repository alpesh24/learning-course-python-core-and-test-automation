class Counter:
    def __init__(self, start=0, stop=None) -> None:
        self.start = start
        self.stop = stop

    def increment(self) -> None:
        if(self.start == self.stop):
            print("The maximal value is reached.")
        else:
            self.start +=1

    def get(self) -> int:
        return self.start
    
c = Counter(start=42)
c.increment()
print(c.get())

c = Counter()
c.increment()
print(c.get())
c.increment()
print(c.get())

c = Counter(start=42, stop=43)
c.increment()
print(c.get())

c.increment()
print(c.get())
