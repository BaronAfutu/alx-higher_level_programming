#!/usr/bin/python3
"""Defines locked class."""


class LockedClass:
    """
    Prevent the user from creating new instances of LockedClass
    attributes for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
