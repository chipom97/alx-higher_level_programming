#!/usr/bin/python3
""" Define a class square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """ A special method that is called 
when an instance of the class is called"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Public instance that returns the area. """

        return (self.__size ** 2)