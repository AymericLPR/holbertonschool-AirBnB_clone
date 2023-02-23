#!/usr/bin/python3
""" Module file_storage for the AirBnB console """
import json

class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        with open(FileStorage.__file_path, "w") as file:
            d = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
            json.dump(d, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, "r") as file:
                d = json.load(file)
                for key, value in d.items():
                    cls_name, obj_id = key.split(".")
                    cls = __import__("models." + cls_name, fromlist=[cls_name])
                    obj = cls.__dict__[cls_name](**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
