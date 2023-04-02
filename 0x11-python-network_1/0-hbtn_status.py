#!/usr/bin/python3

"""
This script fetches the status of https://alx-intranet.hbtn.io/status using
urllib. It displays the response body in three different formats: raw bytes, a
string, and a UTF-8 encoded string.
"""

import urllib.request


def fetch_url():
    """
    Fetches the status of https://alx-intranet.hbtn.io/status using urllib.
    It displays the response body in three different formats: raw bytes, a
    string, and a UTF-8 encoded string.
    """
    url = 'https://alx-intranet.hbtn.io/status'

    with urllib.request.urlopen(url) as response:
        data_func = response.read()

    print("Body response:")
    print("\t- type: {}".format(type(data_func)))
    print("\t- content: {}".format(data_func))
    print("\t- utf8 content: {}".format(data_func.decode('utf-8')))


if __name__ == "__main__":
    fetch_url()
