#!/usr/bin/python3
import datetime
import uuid

class BaseModel:
    
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()
    
    def __init__(self):
        self.id = str(uuid.uuid4())
    
    def __str__(self):
        return f"{type(self).__name__} ({self.id}) {self.__dict__}"
    
    def save(self):
        self.updated_at = datetime.datetime.now()
    
    def to_dict(self):
        self.__dict__ = {"__class__": "f{type(self).__name__}"}
        self.__dict__["created_at"] : {"f{self.created_at.isoformat()}"}
        self.__dict__["updated_at"] : {"f{self.updated_at.isoformat()}"}
        return self.__dict__
