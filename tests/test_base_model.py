#!/usr/bin/env python3

"""Test BaseModel class"""
import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        """Set up the test"""
        self.model = BaseModel()

    def test_init(self):
        """Test the initialization of the BaseModel class"""

        self.assertIsInstance(self.model, BaseModel)
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)
        self.assertTrue(hasattr(self.model, "id"))
        self.assertTrue(hasattr(self.model, "created_at"))
        self.assertTrue(hasattr(self.model, "updated_at"))
        self.assertTrue(hasattr(self.model, "__class__"))
        self.assertTrue(hasattr(self.model, "save"))
        self.assertTrue(hasattr(self.model, "to_dict"))
        self.assertEqual(str(uuid.UUID(self.model.id)), self.model.id)

    def test_str(self):
        """Test the str method of the BaseModel class
        """

        string = f"[{self.model.__class__.__name__}] ({self.model.id}) {self.model.__dict__}"
        self.assertEqual(string, str(self.model))

    def test_save(self):
        """Test the save method of the BaseModel class"""

        current_time = self.model.updated_at
        self.model.save()
        self.assertNotEqual(current_time, self.model.updated_at)

    def test_to_dict(self):
        """Test the to_dict method of the BaseModel class"""
        self.model = BaseModel()
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)


    def test_id(self):
        bm = BaseModel()
        base_model = BaseModel()
        self.assertNotEqual(bm.id, base_model.id)

if __name__ == '__main__':
    unittest.main()
