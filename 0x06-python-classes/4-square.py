#!/usr/bin/python3
"""Defines a Square class"""


class Square:
    """Represents a Square"""
    def __init__(self, size=0):
        """Initializes a Square class by calling setter property

        Parameters:
            size (int): The size of the square. Default is 0.
        """
        self.size = size

    @property
    def size(self):
        """Getter method returns the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size of the Square class.
        Parameters:
            value (int): The size to be set.

        Raises:
            TypeError: If size is not an Integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of the square and returns it"""
        return self.__size ** 2
