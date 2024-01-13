#!/usr/bin/python3
"""Define a function that writes to a file."""


def write_file(filename="", text=""):
    """Writes a string to a UTF8 text file.

    Args:
        filename (str): Name of the file to write.
        text (str): Text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
