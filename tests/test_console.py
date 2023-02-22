#!/usr/bin/python3
"""test for console"""
import unittest
from unittest.mock import patch
from io import StringIO
import os
import json
import console
import tests
from console import HBNBCommand
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestAirBnBConsole(unittest.TestCase):
    """this will test the console"""

    def setUp(self):
        """Sets up test methods."""
        pass


if __name__ == "__main__":
    unittest.main()
