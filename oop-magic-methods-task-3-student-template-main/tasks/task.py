from __future__ import annotations
from typing import Type


class Currency:
    """
    1 EUR = 2 USD = 100 GBP

    1 EUR = 2 USD    ;  1 EUR = 100 GBP
    1 USD = 0.5 EUR  ;  1 USD = 50 GBP
    1 GBP = 0.02 USD ;  1 GBP = 0.01 EUR
    """
    exchage_rates = {
        'EUR' : {'USD':2.0, 'GBP': 100.0, 'EUR': 1},
        'USD' : {'EUR': 0.5, 'GBP': 50.0, 'USD': 1},
        'GBP' : {'EUR': 0.01, 'USD': 0.02, 'GBP': 1}
    }
    cur_map = {
        'Euro' : 'EUR',
        'Dollar': 'USD',
        'Pound' : 'GBP'
    }
    def __init__(self, value: float):
        self.value = value

    @classmethod
    def course(cls, other_cls: Type[Currency]) -> str:
        exchage_rate = cls.exchage_rates[cls.cur_map[cls.__name__]][cls.cur_map[other_cls.__name__]]

        return f"{exchage_rate} {cls.cur_map[other_cls.__name__]} for 1 {cls.cur_map[cls.__name__]}"

    def to_currency(self, other_cls: Type[Currency]):
        exchage_rate = self.exchage_rates[self.cur_map[self.__class__.__name__]][self.cur_map[other_cls.__name__]]
        converted_value = self.value * exchage_rate

        return other_cls(float(converted_value))
    
    def __add__(self, other):
        obj = other.to_currency(self.__class__)
        total = self.value + obj.value
        return self.__class__(total)

    def __str__(self):
        return f"{self.value} {self.cur_map[self.__class__.__name__]}"

class Euro(Currency):
    pass


class Dollar(Currency):
    pass


class Pound(Currency):
    pass


e = Euro(100)
r = Pound(100)
d = Dollar(200)

print(
      f"e + r  =>  {e + r}\n"
      f"r + d  =>  {r + d}\n"
      f"d + e  =>  {d + e}\n"
  )

