def get_fractions(a_b: str, c_b: str) -> str:
    """
    Add your code here  
    """
    a, b  = a_b.split('/')
    c, b = c_b.split('/')
    a, b, c = int(a), int(b), int(c)
    
    return f'{a_b} + {c_b} = {a+c}/{b}'


print(get_fractions('1/3', '5/3'))
