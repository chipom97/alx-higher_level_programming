#!/usr/bin/python3
"""Define a square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square."""
        self.size = size
        self.size = position

    @property
    def size (self):
        """get/set property."""
        return (self.__size = size)

    @size.setter
    def size(self, value):
        """set the value,
        with restrictions"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """get/set property."""
        return (self.__position = position)

    @position.setter
    def position(self, value):
        """set the value,
        with restrictions."""
        if not isinstance(value, int):
            raise TypeError("position must be a tuple of 2 positive integers")
	
	self.__size = value

        def area(self):
            """return cuurent square area."""
            return (self.__size * self.__size)

        def my_print(self):
            """print square with character #."""
            if self.__size < 0:
                print("")
            else:
                
