#!/usr/bin/python3
"""
    defines all common attributes/methods
    for other classes
"""
import uuid
from datetime import datetime
import models


class BaseModel():
    """
    Module: base.py
    """

    def __init__(self, *args, **kwargs):
        """
        initialized an object with it's
        attributes
        """
        date_f = '%Y-%m-%dT%H:%M:%S.%f'
        dates = ['updated_at', 'created_at']
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    pass
                elif key in dates:
                    setattr(self, key, datetime.strptime(value, date_f))

                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

            models.storage.new(self)

    def save(self):
        """
        updates the public instance attribute
        'updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all
        keys/values of __dict__ of the instance
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        try:
            new_dict["created_at"] = self.created_at.isoformat()
            new_dict["updated_at"] = self.updated_at.isoformat()
        except AttributeError:
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            new_dict["created_at"] = self.created_at.isoformat()
            new_dict["updated_at"] = self.updated_at.isoformat()

        return new_dict

    def __str__(self):
        """
        prints [<class_name>] (<self.id>) <self.__dict__>
        """
        class_name = self.__class__.__name__
        ins_id = self.id
        dict_ = self.__dict__

        return "[{}] ({}) {}".format(class_name, ins_id, dict_)
