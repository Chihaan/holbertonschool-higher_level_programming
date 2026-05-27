#!/usr/bin/env python3
"""Module for serializing and deserializing custom objects using pickle."""

import pickle


class CustomObject:
    """A custom object that can be serialized and deserialized using pickle."""

    def __init__(self, name: str, age: int, is_student: bool):
        """Initialize CustomObject with name, age and is_student.

        Args:
            name (str): name of the object.
            age (int): age of the object.
            is_student (bool): whether the object is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes."""
        print(f"Name: {self.name}\n"
              f"Age: {self.age}\n"
              f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the object to a file using pickle.

        Args:
            filename (str): path to the output pickle file.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except (FileNotFoundError, pickle.PicklingError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize and return a CustomObject from a pickle file.

        Args:
            filename (str): path to the input pickle file.

        Returns:
            CustomObject: deserialized object, or None if an error occurs.
        """
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except (FileNotFoundError, pickle.UnpicklingError):
            return None
