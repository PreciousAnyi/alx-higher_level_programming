#!/usr/bin/python3
"""Defines a class named Base"""
import json


class Base:
    """
    Base class for managing id attribute in all future classes.

    Private class attribute:
        __nb_object (int): Number of instantiated Bases.
    """

    __nb_objects = 0

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation
        of list_objs to a file"""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as file:
            json_string = cls.to_json_string([
                obj.to_dictionary() for obj in list_objs])
            file.write(json_string)

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation
        of list_dictionaries"""
        if list_dictionaries is None or
        len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

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
