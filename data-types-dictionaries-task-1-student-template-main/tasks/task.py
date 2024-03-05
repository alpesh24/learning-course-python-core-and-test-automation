from typing import Dict

def get_dict(s: str) -> Dict[str, int]:
    # TODO: Add your code here
    s = s.lower()
    frequency = {}

    for char in s:
        if char in frequency:
            frequency[char]+=1
        else:
            frequency[char]=1
    
    return frequency

print(get_dict('Oh, it is python'))