#!/usr/bin/python3

"""Test BaseModel class"""
import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        """Set up the test"""
        self.model = BaseModel()

    def tearDown(self):
        """Tear down the test"""
        del self.model

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

    def test_init_with_kwargs(self):
        """Test the initialization of the BaseModel class with kwargs"""

        model = BaseModel(id=str(uuid.uuid4()), created_at=datetime.now(), updated_at=datetime.now())
        self.assertIsInstance(model, BaseModel)
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)

    def test_init_without_kwargs(self):
        model = BaseModel()
        self.assertIsNotNone(model.id)
        self.assertIsInstance(model.id, str)
        self.assertIsNotNone(model.created_at)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsNotNone(model.updated_at)
        self.assertIsInstance(model.updated_at, datetime)


    def test_id(self):
        """Test the id of the BaseModel class"""
        bm = BaseModel()
        base_model = BaseModel()
        self.assertNotEqual(bm.id, base_model.id)
        self.assertIsInstance(self.model.id, str)

    def test_created_at(self):
        """Test the created_at of the BaseModel class"""
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at(self):
        """Test the updated_at of the BaseModel class"""
        self.assertIsInstance(self.model.updated_at, datetime)


    def test_str(self):
        """Test the str method of the BaseModel class
        """

        string = f"[{self.model.__class__.__name__}] ({self.model.id}) {self.model.__dict__}"
        self.assertIsInstance(string, str)
        self.assertEqual(string, str(self.model))
        self.assertIn(str(self.model.id), string)
        self.assertIn(str(self.model.__dict__), string)

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
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)


    
    def test_from_dict(self):
        """Test the from_dict method"""
        bm = BaseModel()
        bm_dict = bm.to_dict()
        bm_from_dict = BaseModel.from_dict(bm_dict)
        self.assertEqual(bm.__class__.__name__, bm_from_dict.__class__.__name__)


if __name__ == '__main__':
    unittest.main()