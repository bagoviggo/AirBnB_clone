#!/usr/bin/python3
"""Unittest for City class"""

import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test cases for City"""

    def setUp(self):
        """Set up an instance of City"""
        self.city = City()

    def tearDown(self):
        """Tear down the instance of City"""
        del self.city

    def test_instance(self):
        """Test that the created instance is of the City class"""
        self.assertIsInstance(self.city, City)

    def test_inherits_BaseModel(self):
        """Test that the City class inherits from BaseModel"""
        self.assertTrue(issubclass(City, BaseModel))

    def test_attributes(self):
        """Test that the City class has the required attributes"""
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertTrue(hasattr(self.city, 'name'))

    def test_attributes_type(self):
        """Test that the City class attributes are of the correct type"""
        self.assertIsInstance(self.city.state_id, str)
        self.assertIsInstance(self.city.name, str)

    def test_str_method(self):
        """Test the __str__ method of the City class"""
        expected = "[City] ({}) {}".format(self.city.id, self.city.__dict__)
        self.assertEqual(expected, str(self.city))


if __name__ == '__main__':
    unittest.main()
