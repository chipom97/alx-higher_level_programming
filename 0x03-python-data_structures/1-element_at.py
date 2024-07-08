#!/usr/bin/python3

def element_at(my_list, idx):
    """ function that retrieves an element from a list like """
    if idx < 0 or idx > (len(my_list) - 1):
        return None
    else:
        return (my_list[idx])
