#!/usr/bin/env python3
"""Module for serializing and deserializing data to/from XML files."""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a Python dictionary to an XML file.

    Args:
        dictionary (dict): Python dictionary to serialize.
        filename (str): path to the output XML file.
    """
    root = ET.Element("data")
    for key, item in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(item)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """Deserialize an XML file and return a Python dictionary.

    Args:
        filename (str): path to the input XML file.

    Returns:
        dict: deserialized Python dictionary.
    """
    new_dict = {}
    tree = ET.parse(filename)
    root = tree.getroot()
    for child in root:
        new_dict[child.tag] = child.text
    return new_dict
