#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
import sys

length = len(sys.argv) - 1
operators = ["*", "-", "/", "+"]


def operator():
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if sys.argv[2] == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))
        sys.exit(0)
    elif sys.argv[2] == "-":
        print("{} - {} = {}".format(a, b, sub(a, b)))
        sys.exit(0)
    elif sys.argv[2] == "*":
        print("{} * {} = {}".format(a, b, mul(a, b)))
        sys.exit(0)
    elif sys.argv[2] == "/":
        print("{} / {} = {}".format(a, b, div(a, b)))
        sys.exit(0)


if __name__ == "__main__":
    if length < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    elif length == 3:
        op = sys.argv[2]
        if op in operators:
            operator()
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
