#!/usr/bin/python3
"""Define a function that converts from string to JSON."""
import json


def to_json_string(my_obj):
    """Returns the JSON version of a string object."""
    return json.dumps(my_obj)
