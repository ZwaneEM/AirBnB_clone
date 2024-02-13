#!/usr/bin/python3

"""
    inherits from BaseModel
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Reviews for the place
    """

    place_id = ""
    user_id = ""
    text = ""
