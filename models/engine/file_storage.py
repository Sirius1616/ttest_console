#!/usr/bin/python3
"""The module that depicts the main engine room"""
import json
from models.base_model import BaseModel


class FileStorage:
    """
    The class that will store the dictionary of the attributes
    
    Attributes:
        __file_path: string - path to the JSON file (ex: file.json)
        __objects: dictionary - empty but will store all objects by 
                    <class name>.id (ex: to store a BaseModel
    """
    
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""

        obj_dict = {}

        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()

        with open(self.__file_path, 'w', encoding="UTF-8") as _file:
            json.dump(obj_dict, _file)
        
    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file (__file_path) exists"""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                new_obj_dict = json.load(f)
        except FileNotFoundError:
            pass
