#!/usr/bin/python3
# file_storage.py

"""Defines a FileStorage class that that serializes instances to a JSON file and deserializes JSON file to instances"""
import json

class FileStorage():
    """serializes instances to a JSON file and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects
    
    def new(self, obj):
        """Sets in __objects the obj with the key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj.to_dict()
    
    def save(self):
        """Serializes __objects to the JSON file path"""
        try:
            with open(FileStorage.__file_path, "w") as f:
                json.dump(FileStorage.__objects, f)
        except  Exception as e:
            print("An error occurred:", e)
    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, "r") as f:
                FileStorage.__objects = json.load(f)
        except FileNotFoundError:
            pass