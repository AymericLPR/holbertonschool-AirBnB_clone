#!/usr/bin/python3
""" Comments the module """
import datetime
import uuid

class BaseModel:
""" comment the base Model """    
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()
    
    def __init__(self):
        """ coments """
        self.id = str(uuid.uuid4())
    
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
