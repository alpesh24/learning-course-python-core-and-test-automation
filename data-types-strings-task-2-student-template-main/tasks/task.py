def get_longest_word( s: str) -> str:
    """
     Add your code here 
    """
    str_list = s.split()
    longest_word = str_list[0]

    for word in str_list[1:]:
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word


print(get_longest_word('Python is simple and effective!'))