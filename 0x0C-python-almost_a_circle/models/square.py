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
