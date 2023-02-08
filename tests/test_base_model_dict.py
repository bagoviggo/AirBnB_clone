import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModelMethods(unittest.TestCase):

    def test_from_dict(self):
        """Test the from_dict method"""
        bm = BaseModel()
        bm_dict = bm.to_dict()
        bm_from_dict = BaseModel.from_dict(bm_dict)
        self.assertEqual(bm.__class__.__name__, bm_from_dict.__class__.__name__)
        #convert the datetime objects into Unix timestamps(seconds only) and compare them
        self.assertEqual(int(bm.created_at.timestamp()), int(bm_from_dict.created_at.timestamp())) 
        self.assertEqual(int(bm.updated_at.timestamp()), int(bm_from_dict.updated_at.timestamp()))


if __name__ == '__main__':
    unittest.main()