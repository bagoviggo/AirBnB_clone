#!/usr/bin/env python3
# models/state.py

"""This module inherits from BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """This class defines all attributes for State"""
    name = ""

    def __init__(self, *args, **kwargs):
        """State constructor"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """State string representation"""
        return "[State] ({}) {}".format(self.id, self.__dict__)
