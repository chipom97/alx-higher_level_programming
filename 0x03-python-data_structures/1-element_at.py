#!/usr/bin/python3

def element_at(my_list, idx):
    """ function that retrieves an element from a list like """
    list_len = len(my_list)
    if idx < 0 or idx > (list_len -1):
        return none
    return my_list[idx]
