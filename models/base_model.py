#!/usr/bin/python3
""" Comments the module """
import datetime
import uuid

class BaseModel:
    """Base class for all models"""

    def __init__(self, *args, **kwargs):
        """Initialize a new instance of BaseModel"""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
 
    def __str__(self):
        """ comments """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        """ comments """
        self.updated_at = datetime.datetime.now()
    
    def to_dict(self):
        """ comments """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = type(self).__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
