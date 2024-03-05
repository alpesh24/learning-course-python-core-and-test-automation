def union(*args) -> set:
    result_set = set()
    for a in args:
        result_set = result_set.union(a)
    
    return result_set


def intersect(*args) -> set:
    result_set = set(args[0])
    for a in args[1:]:
        result_set = result_set.intersection(a)

    return result_set



print(union(('S', 'A', 'M'), ['S', 'P', 'A', 'C']))
print(intersect(('S', 'A', 'C'), ('P', 'C', 'S'), ('G', 'H', 'S', 'C')))