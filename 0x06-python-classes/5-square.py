#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize the square,
        with default public attributer"""
        self.size = size

    @property
    def size(self):
        """get/set size of square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """set a value for size,
        with restrictions."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of th e square."""
        return (self.__size * self.__size)

    def my_print(self):
        """print the square with the # character."""
        if self.size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")
