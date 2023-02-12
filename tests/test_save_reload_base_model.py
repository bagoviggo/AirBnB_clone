import unittest
import json
from io import StringIO
from unittest.mock import patch
import os
from engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_storage = FileStorage()

    def tearDown(self):
        try:
            os.remove("file.json")
        except:
            pass

    def test_all_method(self):
        self.file_storage.new({"object1": {"id": 1}})
        result = self.file_storage.all()
        self.assertEqual(result, {"object1": {"id": 1}})

    def test_new_method(self):
        class TestClass():
            def __init__(self, id, name):
                self.id = id
                self.name = name
            def to_dict(self):
                return {"id": self.id, "name": self.name}
        test_obj = TestClass(1, "test")
        self.file_storage.new(test_obj)
        result = self.file_storage.all()
        self.assertEqual(result, {"TestClass.1": {"id": 1, "name": "test"}})

    def test_save_method(self):
        self.file_storage.__objects = {"object1": {"id": 1}}
        self.file_storage.save()
        with open("file.json", "r") as f:
            result = json.load(f)
        self.assertEqual(result, {"object1": {"id": 1}})

    def test_reload_method(self):
        self.file_storage.__objects = {"object1": {"id": 1}}
        self.file_storage.save()
        self.file_storage.__objects = {}
        self.file_storage.reload()
        result = self.file_storage.all()
        self.assertEqual(result, {"object1": {"id": 1}})

    def test_reload_method_file_not_found(self):
        with patch('builtins.print') as mock_print:
            self.file_storage.reload()
            mock_print.assert_not_called()

if __name__ == '__main__':
    unittest.main()
