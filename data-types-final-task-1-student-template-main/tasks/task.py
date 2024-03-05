from typing import Any, Dict, List, Set

def check(lst: List[Dict[Any, Any]]) -> Set[Any]:
    """
    Add your code here or call it from here   
    """
    values = []

    for d in lst:
        dict_val = d.values()
        for v in dict_val:
            values.append(v)

    set_values = set(values)
    return set_values


l = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
print(check(l))
