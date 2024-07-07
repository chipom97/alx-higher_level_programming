#!/usr/bin/python3

if __name__ == "__main__":
    """prints the result of the addition of all arguments"""
    import sys

    num_args = len(sys.argv) - 1
    i = num_args
    total = 0
    while (i > 0):
        total += int(sys.argv[i])
        i -= 1

    print(total)
