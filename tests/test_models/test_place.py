#!/usr/bin/python3
"""
Unittest for Place
"""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """
    Test cases for Place
    """
    def setUp(self):
        """
        Sets up an instance of Place to test
        """
        self.place = Place()

    def test_place_attributes(self):
        """
        Tests that Place attributes are present
        """
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertTrue(hasattr(self.place, "name"))
        self.assertTrue(hasattr(self.place, "description"))
        self.assertTrue(hasattr(self.place, "number_rooms"))
        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        self.assertTrue(hasattr(self.place, "max_guest"))
        self.assertTrue(hasattr(self.place, "price_by_night"))
        self.assertTrue(hasattr(self.place, "latitude"))
        self.assertTrue(hasattr(self.place, "longitude"))
        self.assertTrue(hasattr(self.place, "amenity_ids"))

    def test_place_instance(self):
        """
        Tests that Place is an instance of BaseModel
        """
        self.assertIsInstance(self.place, BaseModel)

    def test_place_str_representation(self):
        """
        Tests that __str__ method returns the correct string representation
        """
        place_str = str(self.place)
        self.assertTrue("[Place]" in place_str)
        self.assertTrue("id" in place_str)
        self.assertTrue("created_at" in place_str)
        self.assertTrue("updated_at" in place_str)


if __name__ == '__main__':
    unittest.main()
