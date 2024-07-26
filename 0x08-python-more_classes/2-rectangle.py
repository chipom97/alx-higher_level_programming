#!/usr/bin/python3
"""Define a class rectangle"""


class Rectangle:
    """represent a class rectangle"""

    def __init__(self, width=0, height=0):
        """initialise a new rectangle,
        with public attributes"""
        self.width = width
        self.height = height

    @property
    def width(self):
        "return the width of rectangle"
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        "return the height of the rectangle"
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return the area of the rectange"""
        return (self.__width * self.__height)

    def perimeter(self):
        """return the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return ((self.__width * 2) + (self.__height * 2))
