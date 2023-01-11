#!/usr/bin/python3
"""function that creates an object from a JSON file
"""

import json


def load_from_json_file(filename):
    """create a python object froma JSON file"""
    with open(filename) as f:
        return json.load(f)
