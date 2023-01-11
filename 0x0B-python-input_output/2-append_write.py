#!/usr/bin/python3
"""
function that appends the string of a text file (UTF8) and returns the number
of the strings added
"""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF8 text file
    args:
        filename(str): the name of the file to append to
        text(str): the string to append to the file
    return:
        the number of characters appended
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
