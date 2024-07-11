#!/usr/bin/python3

def uniq_add(my_list=[]):
    """function that adds all unique integers in a list"""
    present = set()
    result = 0
    for num in my_list:
        if num not in present:
            result += num
            present.add(num)
    return result
