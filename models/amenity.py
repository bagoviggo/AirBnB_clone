#!/usr/bin/env python3
# models/amenity.py

"""This module inherits from BaseModel"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """This class defines all attributes for Amenity"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Amenity constructor"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """Amenity string representation"""
        return "[Amenity] ({}) {}".format(self.id, self.__dict__)
