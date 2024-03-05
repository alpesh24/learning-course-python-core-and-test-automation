from typing import Dict

def generate_squares(num: int)-> Dict[int, int]:
    """
    Add your code here or call it from here   
    """
    result_dict = {}
    for x in range(1, num+1):
        result_dict.update({x: x**2})
    

    return result_dict

print(generate_squares(5))