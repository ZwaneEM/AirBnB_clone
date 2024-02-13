#!/usr/bin/python3

"""
    class that inherits from BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    creates a new User
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
