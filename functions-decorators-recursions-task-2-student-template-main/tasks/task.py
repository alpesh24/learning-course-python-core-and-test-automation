from typing import Any, List, Tuple

def linear_seq(sequence: List[Any]) -> List[Any]:
    """
    Add your code here or call it from here   
    """
    res = []
    for el in sequence:
        if isinstance(el,List) or isinstance(el, Tuple):
            res.extend(linear_seq(el))
        else:
            res.append(el)
    
    return res

sequence =  [1, 2, (3, [4, [5, (6, [7])]])]
print(linear_seq(sequence))
