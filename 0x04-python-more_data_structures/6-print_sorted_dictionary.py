#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """function that prints a dictionary by ordered keys"""
    for key, value in sorted(a_dictionary.items()):
        print("{}: {}".format(key, value))
