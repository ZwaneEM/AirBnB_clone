#!/usr/bin/python3

"""
serializes instances to a JSON file
and deserializes JSON file to instances
"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from datetime import datetime


class FileStorage():
    """
    Module: file_storage.py
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key
        <obj class name>.id
        """
        obj_name = obj.__class__.__name__
        key_obj = "{}.{}".format(obj_name, obj.id)

        self.__objects[key_obj] = obj

    def save(self):
        """
        Serializes __objects to the JSON file
        """
        final_obj = {}

        for key, value in self.__objects.items():
            final_obj[key] = value.to_dict()

        with open(self.__file_path, "w", encoding="utf-8") as file:
            file.write(json.dumps(final_obj))

    def reload(self):
        """
        Deserializes the JSON file to __objects
        * Only if the JSON file exits
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as file:
                data = json.loads(file.read())

            for key, value in data.items():
                class_name = key.split(".")[0]
                self.new(eval(class_name)(**value))
