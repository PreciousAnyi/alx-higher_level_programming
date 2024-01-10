#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    new_set1 = set(filter(lambda x: x not in set_1, set_2))
    new_set2 = set(filter(lambda x: x not in set_2, set_1))
    result = new_set1.union(new_set2)
    return result
