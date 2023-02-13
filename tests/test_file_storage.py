#!/usr/bin/env python3

"""Unittest for FileStorage class"""
import unittest
import json
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test FileStorage class"""

    def setUp(self):
        """Set up the test"""
        self.storage = FileStorage()
        self.storage.FileStorage__objects = {}
        self.storage.FileStorage__objects.clear()

    def tearDown(self):
        """Tear down the test"""
        with open("file.json", "w") as f:
            json.dump({}, f)

    def test_save_method_empty(self):
        self.storage.save()
        with open("file.json", "r") as f:
            self.assertEqual(json.load(f), self.storage.all())

    def test_save_method_not_empty(self):
        obj = {"id": "123", "name": "test_obj"}
        key = "TestObject.123"
        self.storage._FileStorage__objects[key] = obj
        self.storage.save()
        with open("file.json", "r") as f:
            self.assertEqual(json.load(f), {key: obj})

    def test_reload_method_file_present(self):
        obj = {"id": "123", "name": "test_obj"}
        key = "TestObject.123"
        with open("file.json", "w") as f:
            json.dump({key: obj}, f)
        self.storage.reload()
        self.assertEqual(self.storage.all(), {key: obj})

    def test_reload_method_file_not_present(self):
        with open("file.json", "w") as f:
            json.dump({}, f)
        self.storage.reload()
        with open("file.json", "r") as f:
            self.assertEqual(json.load(f), self.storage.all())


if __name__ == '__main__':
    unittest.main()
