from typing import Tuple

def get_tuple(num: int) -> Tuple[int]:
    # TODO: Add your code here
    
    digits = [int(digit) for digit in str(num)]

    return tuple(digits)

print(get_tuple(87178291199))