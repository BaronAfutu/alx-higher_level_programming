#!/usr/bin/python3
"""Define a function that appends text to a file."""


def append_write(filename="", text=""):
    """Append a string to the end of a UTF8 text file.

    Args:
        filename (str): Name of the file to append to.
        text (str): String to append to the file.
    Returns:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
