#!/usr/bin/env python3
"""Module for serializing and deserializing data to/from JSON files."""

import json


def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary to a JSON file.

    Args:
        data (dict): Python dictionary to serialize.
        filename (str): path to the output JSON file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load and deserialize a JSON file to a Python dictionary.

    Args:
        filename (str): path to the input JSON file.

    Returns:
        dict: deserialized Python dictionary.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
