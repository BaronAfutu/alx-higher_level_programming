#!/usr/bin/python3
"""Define a square-printing function."""


def print_square(size):
    """Prints a square with the # character.

    Args:
        size (int): height/width of the square.
    Raises:
        TypeError: size is not an integer.
        ValueError: size is < negative
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
