from typing import Union, List

ListType = List[Union[int, str]]


def get_fizzbuzz_list(n: int) -> ListType:
    # TODO: Add your code here
    res = [i for i in range(1, n+1)]

    for i, x in enumerate(res):
        if x % 3 == 0 and x % 5 == 0:
            res[i] = 'FizzBuzz'
        elif x % 3 == 0:
            res[i] = 'Fizz'
        elif x % 5 == 0:
            res[i] = 'Buzz'
        else:
            continue
        
    return res

print(get_fizzbuzz_list(15))