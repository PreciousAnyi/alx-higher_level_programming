#!/usr/bin/python3
"""Defines a class named Base"""
class Base:
    """
    Base class for managing id attribute in all future classes.
    
    Private class attribute:
        __nb_object (int): Number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for the Base class.

        Attributes:
            id (int, optional): The id of the object. If provided, sets the id
                attribute to this value. If not provided, increments the
                private class attribute __nb_objects and assigns the new
                value to the id attribute.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
