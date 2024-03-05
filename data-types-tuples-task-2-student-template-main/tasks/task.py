from typing import Any, Tuple, List

def get_pairs(lst: List[Any]) -> List[Tuple[Any, Any]]:
    # TODO: Add your code here
    if len(lst) <= 1:
        return []
    
    res = []
    for i in range(0, len(lst)-1):
        t = (lst[i], lst[i+1])
        res.append(t)

    return res


print(get_pairs([1, 2, 3, 8, 9]))
print(get_pairs(['need', 'to', 'sleep', 'more']))
print(get_pairs([1]))