#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """function that prints all integers of a list, in reverse order."""
    if my_list is None:
        return

    reversed_list = list(reversed(my_list))
    for num in reversed_list:
        print("{:d}".format(num))
