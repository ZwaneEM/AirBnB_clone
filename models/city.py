#!/usr/bin/python3

"""
    Inherits from BaseModel
"""

from models.base_model import BaseModel


class City(BaseModel):

    """
    Represents a city
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a city Instance
        """
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""
