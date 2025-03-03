#!/usr/bin/python3

def element_at(my_list, idx):
    length = len(my_list) - 1
    if idx < -1 or idx > length:
        return None
    else:
        for i in range(len(my_list)):
            if i == idx:
                return my_list[i]
