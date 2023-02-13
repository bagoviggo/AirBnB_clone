#!/usr/bin/env python3
# models/city.py

"""This module inherits from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """This class defines all attributes for City"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """City constructor"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """City string representation"""
        return "[City] ({}) {}".format(self.id, self.__dict__)
