from typing import List, Dict

def combine_dicts(*args:List[Dict[str, int]]) -> Dict[str, int]:
    result_dict = {}

    for dic in args:
        keys = dic.keys()
        for k in keys:
            if k in result_dict:
                result_dict[k]+=dic[k]
            else:
                result_dict[k] = dic[k]
    
    return result_dict


dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}


print(combine_dicts(dict_1, dict_2))
print(combine_dicts(dict_1, dict_2, dict_3))
