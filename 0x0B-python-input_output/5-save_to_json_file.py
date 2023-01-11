#!/usr/bin/python3
"""function that writes an object to a text file, using a JSON representation
"""

import json


def save_to_json(my_obj, filename):
    """module save_to_json_file
    accepts python objects and sends JSON representation to file
    """
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
