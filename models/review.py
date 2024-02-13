#!/usr/bin/python3

"""
    inherits from BaseModel
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Reviews for the place
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a Review instance
        """
        super().__init__(*args, **kwargs)

        self.place_id = ""
        self.user_id = ""
        self.text = ""
