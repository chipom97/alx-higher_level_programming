#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if not row:
            print()
            continue
        lst_ind = len(row) - 1
        num = row[lst_ind]
        for i in row:
            if i == num:
                print("{:d}".format(i))
            else:
                print("{:d}".format(i), end=" ")
