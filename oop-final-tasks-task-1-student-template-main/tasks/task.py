class Sun:
    _instance = None

    def __init__(self):
        raise RuntimeError("Call Sun.inst() to create an instance")

    @classmethod
    def inst(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
        return cls._instance
    
p = Sun.inst()
f = Sun.inst()
print(p is f)
