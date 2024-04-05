#!/usr/bin/python3
""" Define a class square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Function called when instance of class is created"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Public instance that returns the area. """

        return (self.__size ** 2)
