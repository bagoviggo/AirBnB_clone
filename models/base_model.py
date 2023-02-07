#!/usr/bin/python3
# base_models.py

"""Defines a  base class for all the other classes in this project"""
import uuid
import datetime

class BaseModel():
    """Define all common attributes/methods for the other classes
    to take care of initialization, serialization and deserialization
    of future instances"""

    def __init__(self, *args, **kwargs):
        """Initializes every instance of BaseModel
            Args:
                id (str): Uniqued id to identify the instance
                created_at (datetime): current datetime an instance is created
                updated_at (datetime): current datetime an instance is updated
        """
        if kwargs is not None:
            self.id = kwargs.get('id', "default1")
            self.created_at = kwargs.get('created_at')
            self.updated_at = kwargs.get('updated_at')
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """Returns a string that prints the format
            [<class name>] (<self.id>) <self.__dict__>
        """
        string = "[" + str(self.__class__.__name__) + "] "
        string += "(" + str(self.id) + ")"
        string += str(self.__dict__)
        return (string)

    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__ of the instance"""
        dict_a = self.__dict__
        class_model = {
                '__class__':self.__class__.__name__, 
                'created_at': self.created_at.isoformat(), 
                'updated_at': self.updated_at.isoformat()
                }
        dict_a.update(class_model)
        return (dict_a)
