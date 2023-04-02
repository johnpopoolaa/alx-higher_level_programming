#!/usr/bin/python3

"""
This script fetches a url using the package 'urllib' and a 'with' statement
"""

import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            read_func = response.read().decode('utf-8')

        print(read_func)

    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
