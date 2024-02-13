#!/usr/bin/python3

"""
    Inherits from BaseModel
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    State of the property
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a State instance
        """

        self.name = ""
