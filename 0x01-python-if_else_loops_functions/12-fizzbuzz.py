#!/usr/bin/python3

def fizzbuzz():
    """ prints the numbers from 1 to 100 separated by a space.
    multiples of three print Fizz, multiples of five print Buzz,
    multiples of both three and five print FizzBuzz."""
    for i in range(1, 101):
        if (i % 15 == 0):
            print("FizzBuzz ", end="")
        elif (i % 3 == 0):
            print("Fizz ", end="")
        elif (i % 5 == 0):
            print("Buzz ", end="")
        else:
            print("{} ".format(i), end="")
