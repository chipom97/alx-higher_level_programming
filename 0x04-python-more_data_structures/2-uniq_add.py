#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    uniq_list = []
    for element in my_list:
        if element not in uniq_list:
            uniq_list.append(element)
    for element in uniq_list:
        result += element
    return result
