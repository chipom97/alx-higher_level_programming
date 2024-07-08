#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """replace an element, without modifying the original list"""
    new_list = my_list[:]
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list
    else:
        new_list[idx] = element
        return new_list
