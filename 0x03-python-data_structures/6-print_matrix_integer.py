#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """function that prints a matrix of integers."""
    for inner in matrix:
        for num in inner:
            if num == inner[(len(inner) - 1)]:
                print("{:d}".format(num), end="")
            else:
                print("{:d}".format(num), end =" ")
        print()
