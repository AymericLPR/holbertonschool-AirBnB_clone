#!/usr/bin/python3
"""user class"""
from models.base_model import BaseModel


class User(BaseModel):
    """class for user with attributes:
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
