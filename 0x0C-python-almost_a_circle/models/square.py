#!/usr/bin/python3
"""Defines a class named Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Inistialize using super call"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overloading __str__"""
        return f"[Square] ({self.id}) {self.x}/{self.y}" \
            f" - {self.width}"

    @property
    def size(self):
        """Gets size of square"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns attributes to the square"""
        if args:
            attr = ["id", "size", "x", "y"]
            for i, arg in enumerate(args[:len(attr)]):
                setattr(self, attr[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation
        of a Square"""
        return {
                'id': self.id,
                'x': self.x,
                'size': self.size,
                'y': self.y
        }

    def __str__(self):
        """Returns a string representation
        of the square"""
        return f"[Square] ({self.id}) {self.x}/{self.y}" \
            f" - {self.size}"
