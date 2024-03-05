def check_str(s: str):
    """
    Add your code here
    """
    string = s.lower()
    string_alpha = list([val for val in string if val.isalpha()])
    res = "".join(string_alpha)
    
    left, right = 0, len(res)-1

    if len(res) <= 1:
        return True
    while left <= right:
        if(res[left] != res[right]):
            return False
        else:
            left+=1
            right-=1
    return True

print(check_str("A dog! A panic in a pagoda!"))
print(check_str("Do nine men Interpret? Nine men I nod"))
print(check_str("T. Eliot, top bard, notes putrid tang emanating, is sad; I'd assign it a name: gnat dirt upset on drab pot toilet."))
print(check_str("A man, a plan, a canal — Panama!"))
print(check_str("rotor"))
print(check_str("anavolimilovana"))
