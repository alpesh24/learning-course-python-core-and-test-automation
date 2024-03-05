from typing import List


def foo(nums: List[int]) -> List[int]:
    # TODO: Add your code here
    product = 1
    for x in nums:
        product*=x
    
    res = [product//i for i in nums]
    
    return res


print(foo([1, 2, 3, 4, 5]))
print(foo([3, 2, 1]))