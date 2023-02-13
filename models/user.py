#!/usr/bin/python3
# models/user.py

"""This module inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """This class defines all attributes for User"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """User constructor"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """User string representation"""
        return "[User] ({}) {}".format(self.id, self.__dict__)
