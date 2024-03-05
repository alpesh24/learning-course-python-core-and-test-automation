from typing import List

def check(row_start:int, row_end:int, column_start:int, column_end:int) -> List[List[int]]:
    """
    Add your code here or call it from here   
    """
    all_results = []

    row = [x for x in range(row_start, row_end+1)]
    col = [y for y in range(column_start, column_end+1)]

    for i in row:
        results = [i * x for x in col]
        all_results.append(results)
    
    return all_results

print(check(2, 4, 3, 7))