#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    num = len(argv) - 1
    total = 0

    for arg in argv[1:]:
        arg = int(arg)
        total += arg

    print(total)
