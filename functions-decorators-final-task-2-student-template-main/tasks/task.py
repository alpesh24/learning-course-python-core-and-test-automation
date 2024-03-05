from typing import List

def split_by_index(s: str, indexes: List[int]) -> List[str]:
    """
    Add your code here or call it from here   
    """
    result = []

    old_index = 0

    for i, x in enumerate(indexes):
        #print(f"old index={old_index}, index={x}")
        if x not in range(0, len(s)-1):
            result.clear()
            result.append(s)
            break
        
        string = s[old_index:x]
        #print(string)
        result.append(string)
        old_index = x

        if i == len(indexes)-1:
            last = s[x::]
            #print(last)
            result.append(last)

    return result

print(split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]))
print(split_by_index("no luck", [42]))