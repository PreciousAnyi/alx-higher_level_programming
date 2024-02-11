#!/usr/bin/python3
"""Defines a class named Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Defines a new Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):

        """
        Initializes a new Rectangle
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Gets the width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of a Rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of a Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of a Rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > o")
        self.__height = value

    @property
    def x(self):
        """Gets x value"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets x value"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get y value"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets y value"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
