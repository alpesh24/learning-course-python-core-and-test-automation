def replacer(s: str) -> str:
    """
    Add your code here
    """
    tmp_idx = [pos for pos, char in enumerate(s) if char=="'"]
    result = list(s.replace('"', "'"))
    for idx in tmp_idx:
        result[idx] = '"'
    
    return "".join(result)

print(replacer(f'Implement a function that receives a string and replaces all " symbols with \'quotes\' and vice versa.'))