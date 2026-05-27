#!/usr/bin/env python3
"""Module for converting CSV files to JSON format."""

import csv
import json


def convert_csv_to_json(filename):
    """Convert a CSV file to JSON format and save it to data.json.

    Args:
        filename (str): path to the input CSV file.

    Returns:
        bool: True if conversion was successful, False otherwise.
    """
    dict_list = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            dict_list = list(reader)
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(dict_list, f)
            return True
    except FileNotFoundError:
        return False
