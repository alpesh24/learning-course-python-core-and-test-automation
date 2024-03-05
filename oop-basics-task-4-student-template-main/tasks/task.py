from typing import Dict


class HistoryDict:
    def __init__(self, dict:Dict) -> None:
        self.history = []
        self.dict = dict

    def set_value(self, key, value) -> None:
        self.dict.update({key:value})
        self.history.append(key)
        if(len(self.history)==6):
            self.history.pop(0)

    def get_history(self) -> []:
        return self.history

d = HistoryDict({"foo": 42})
print(d.dict)
d.set_value("bar", 43)
print(d.dict)
print(d.get_history())

d.set_value("foo", 44)
print(d.get_history())
