#!/usr/bin/python3

"""
This script takes in a URL, sends a request to the URL, and displays the body
of the response. If the HTTP status code is greater than or equal to 400, an
error code followed by the value of the HTTP status code is printed.
"""

import requests
import sys


def main():
    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)


if __name__ == "__main__":
    main()
