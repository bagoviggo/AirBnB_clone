#!/usr/bin/python3
"""Unittest module for Review class"""

import unittest
from models.review import Review
from models.base_model import BaseModel

class TestReview(unittest.TestCase):
    """Test cases for Review class"""

    def test_attributes(self):
        """Test Review attributes"""
        r = Review()
        self.assertTrue(hasattr(r, 'place_id'))
        self.assertEqual(r.place_id, "")
        self.assertTrue(hasattr(r, 'user_id'))
        self.assertEqual(r.user_id, "")
        self.assertTrue(hasattr(r, 'text'))
        self.assertEqual(r.text, "")

    def test_inheritance(self):
        """Test Review inheritance"""
        r = Review()
        self.assertIsInstance(r, Review)
        self.assertIsInstance(r, BaseModel)

    def test_str(self):
        """Test Review string representation"""
        r = Review()
        s = "[Review] ({}) {}".format(r.id, r.__dict__)
        self.assertEqual(str(r), s)

if __name__ == '__main__':
    unittest.main()
