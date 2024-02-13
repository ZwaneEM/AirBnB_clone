#!/usr/bin/python3

"""
    inherits from BaseModel
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Represents a Place
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a Place Instance
        """
        super().__init__(*args, **kwargs)

        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitute = 0.0
        self.longitute = 0.0
        self.amenity_ids = []
