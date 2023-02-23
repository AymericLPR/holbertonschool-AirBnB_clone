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
        """ method that loads the objectos from de file """
        from models.base_model import BaseModel
        from models.user import User
        try:
            with open(FileStorage.__file_path) as fp:
                data = json.load(fp)
                for i, j in data.items():
                    if "BaseModel" in i:
                        self.__objects[i] = BaseModel(**j)
                    elif "User" in i:
                        self.__objects[i] = User(**j)
        except Exception:
            pass
