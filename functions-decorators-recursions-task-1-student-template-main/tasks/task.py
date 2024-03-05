from typing import List, Tuple, Union


def seq_sum(sequence: Union[List, Tuple]) -> int:
    """
    Add your code here or call it from here   
    """
    sum = 0
    for el in sequence:
        if isinstance(el,List) or isinstance(el, Tuple):
            sum += seq_sum(el)
        else:
            sum+=el
    
    return sum

sequence = [1,2,3,[4,5, (6,7)]]
sequence_2 = (1,2,3,[4,5],[(6,7), 1, [1, 1], ([1,1, (1,1)])])
print(seq_sum(sequence_2))
