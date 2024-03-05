from typing import List

def split(data: str, sep=None, maxsplit=-1):
    """
    Add your code here or call it from here   
    """
    if not data:
        return []
    
    if sep is None: # if separator is space
        parts=[]
        current_part = ''
        split_count = 0

        index = data.find(" ")
        if index == -1:
            parts.append(data)
            return parts

        string = data.strip()
        if maxsplit == 0:
            parts.append(string)
            return parts
        
        for char in string:
            if char == ' ':
                if maxsplit != split_count:
                    parts.append(current_part)
                    current_part = ''
                    split_count += 1
                    if split_count == maxsplit:
                       second_string = string[string.index(char):]
                       second_to_add = second_string.strip()
                       parts.append(second_to_add) 
                       break
                    
            else:
                current_part += char

        return parts

    
    else:
        parts = []
        current_part = ''
        split_count = 0

        index = data.find(sep)
        if (index ==-1):
            parts.append(data)
            return parts
        first_char = 0
        if(maxsplit == 0):
            parts.append(data)
        while(split_count != maxsplit and (index != -1 and index<len(data))):

            current_part+= data[first_char:index]
            parts.append(current_part)
            first_char = index + len(sep)
            split_count+=1
            current_part=''
            
            if(index == len(data)-1):
                parts.append(current_part)
            if(first_char >= len(data)):
                break
            index = data.find(sep, first_char)
        
        return parts

if __name__ == '__main__':
    assert split('') == []
    assert split(',123,', sep=',') == ['', '123', '']
    assert split('test') == ['test']
    assert split('Python    2     3', maxsplit=1) == ['Python', '2     3']
    assert split('    test     6    7', maxsplit=1) == ['test', '6    7']
    assert split('    Hi     8    9', maxsplit=0) == ['Hi     8    9']
    assert split('    set   3     4') == ['set', '3', '4']
    assert split('set;:23', sep=';:', maxsplit=0) == ['set;:23']
    assert split('set;:;:23', sep=';:', maxsplit=2) == ['set', '', '23']

    #print(split(''))
    #print(split(',123,', sep=','))
    #print(split('test'))
    #print(split('Python    2     3', maxsplit=1))
    #print(split('    test     6    7', maxsplit=1))
    #print(split('    Hi     8    9', maxsplit=0))
    print(split('    set   3     4'))
    #print(split('set;:23', sep=';:', maxsplit=0))
    print(split('set;:;:23', sep=';:', maxsplit=2))
