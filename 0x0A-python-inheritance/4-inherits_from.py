#!/usr/bin/python3
"""Defines a function that checks an inherited class."""


def inherits_from(obj, a_class):
    """Checks if object obj is an inherited instance of class a_class.

    Args:
        obj (any): Object to check.
        a_class (type): Class to match the type of obj to.
    Returns:
        If obj is an inherited instance of a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
