#!/usr/bin/python3
"""Defines a function that checks class instance."""


def is_same_class(obj, a_class):
    """Checks if object obj  is exactly an instance of a_class.

    Args:
        obj (any): Object to check.
        a_class (type): Class to match the type of obj to.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
