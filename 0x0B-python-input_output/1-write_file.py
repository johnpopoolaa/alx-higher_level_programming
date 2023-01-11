#!/usr/bin/python3
"""
funcion that writes a string to a tezt file and returns
the number of characters written
"""


def write_file(filename"", text=""):
    """
    module write_file
    """
    with open(filename, 'w')as f:
        return f.write(text)
