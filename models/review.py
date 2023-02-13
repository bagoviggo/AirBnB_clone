#!/usr/bin/env python3
# models/review.py

"""This module inherits from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """This class defines all attributes for Review"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Review constructor"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """Review string representation"""
        return "[Review] ({}) {}".format(self.id, self.__dict__)
