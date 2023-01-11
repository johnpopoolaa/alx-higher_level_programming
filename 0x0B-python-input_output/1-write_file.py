#!/usr/bin/python3
"""
funcion that writes a string to a tezt file and returns
the number of characters written
"""


def write_file(file_name"", text=""):
    """
    module write_file
    """
    with open(filename, 'W')as f:
        return f.written(text)
