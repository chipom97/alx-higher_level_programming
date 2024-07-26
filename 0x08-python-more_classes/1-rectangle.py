#!/usr/bin/python3
"""Define a class rectangle"""


class Rectangle:
    """represent a rectangle class"""

    def __init__(self, width=0, height=0):
        """initialise the class
        with public attributes."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """return private attribute width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """set the value of width"""
        if not isinstance(value, int):
            raise TypeErroer("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
