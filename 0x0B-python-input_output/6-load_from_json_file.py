#!/usr/bin/python3
"""Define a function that reads JSON file."""
import json


def load_from_json_file(filename):
    """Creates a Python object from a JSON file."""
    with open(filename) as f:
        return json.load(f)
