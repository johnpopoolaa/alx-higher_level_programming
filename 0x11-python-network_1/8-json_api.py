#!/usr/bin/python3

"""
This module sends a POST request to http://0.0.0.0:5000/search_user
with a letter as a parameter
"""

import requests
import sys


def search_user():
    """
    Sends a POST request to http://0.0.0.0:5000/search_user with a letter as a
    parameter
    """

    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    try:
        response = requests.post(url, data={'q': q})
        data = response.json()
        if data:
            print("[{}] {}".format(data.get('id'), data.get('name')))
        else:
            print("No result")
    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    search_user()
