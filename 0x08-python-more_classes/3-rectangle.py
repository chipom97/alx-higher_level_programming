#!/usr/bin/python3
"""Class that defines a rectange."""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """initialise rectangle class"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """return value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the value og width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Return the private attribute of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the value of height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

        
    def area(self):
        """return area of rectangle."""
        return (self.__height * self.__width)
    
    def perimeter(self):
        """Return rectangle perimeter."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.__width + self.heigh)

    def __str__(self):
        """print the rectangle with the character #"""
        if self.width == 0 or self.height == 0:
            return ""
        
