#!/usr/bin/python3

"""script fetches a url using the package 'urllib' and a 'with' statement"""

import urllib.request


def fetch_url(url):

    """fetches a url"""

    r = urllib.request.Request(url)

    with urllib.request.urlopen(r) as response:
        read_func = response.read()

    print("Body response:")
    print(f"\t- type: {type(read_func)}")
    print(f"\t- content: {read_func}")
    print(f"\t- utf-8 content: {read_func.decode('utf-8')}")


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    fetch_url(url)
