#!/usr/bin/python3

"""
Module to fetch https://alx-intranet.hbtn.io/status using requests module
"""

import requests


def fetch_url():
    """
    Function that fetches https://alx-intranet.hbtn.io/status using requests
    module
    """
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))


if __name__ == "__main__":
    fetch_url()
