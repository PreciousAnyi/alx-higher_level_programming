#!/usr/bin/python3
"""Defines unittests for base.py.

Unittest classes:
    TestBase_instantiation

"""
import os
import unittest
from models.base import Base


class TestBaseInstantiation(unittest.TestCase):
    """Unit tests for Base class instantiation."""

    def test_default_id_incremented(self):
        """Test that each instantiation of Base without
        an ID increments the ID.
        """
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id + 1, base2.id)

    def test_id_provided(self):
        """Test that Base assigns the provided
        ID if given.
        """
        base = Base(12)
        self.assertEqual(12, base.id)

    def test_id_is_unique(self):
        """Test that Base assigns unique IDs."""
        base1 = Base()
        base2 = Base(12)
        base3 = Base()
        self.assertNotEqual(base1.id, base3.id)

    def test_id_can_be_changed(self):
        """Test that the ID attribute of Base is
        public and can be changed.
        """
        base = Base(12)
        base.id = 15
        self.assertEqual(15, base.id)

    def test_nb_instances_private(self):
        """Test that __nb_instances attribute is private."""
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_too_many_args(self):
        """Test that Base raises TypeError when
        provided with too many arguments.
        """
        with self.assertRaises(TypeError):
            Base(1, 2)


if __name__ == '__main__':
    unittest.main()
