#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    od_set = set()
    for elem1 in set_1:
        if elem1 not in set_2:
            od_set.add(elem1)
    for elem2 in set_2:
        if elem2 not in set_1:
            od_set.add(elem2)
    return od_set
