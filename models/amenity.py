#!/usr/bin/pytho3

"""
    inherits from BaseModel
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Represents an Amenity
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new Amenity instance
        """
        super().__init__(*args, *kwargs)
        self.name = ""
