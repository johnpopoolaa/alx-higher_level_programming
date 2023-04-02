#!/usr/bin/python3

"""
This script takes a URL as an argument, sends a request to the URL, and
displays the value of the X-Request-Id header in the response.
"""

import urllib.request
import sys


def get_request_id(url):
    """
    Send a request to a specified URL and return the value of the
    'X-Request-Id' header
    """
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        header = response.info()
        if 'X-Request-Id' in header:
            return header['X-Request-Id']


if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = sys.argv[1]
        request_id = get_request_id(url)
        if request_id:
            print(request_id)
