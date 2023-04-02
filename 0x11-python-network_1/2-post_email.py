#!/usr/bin/python3

"""
This module takes in a URL and an email, sends a POST request to the passed
URL with the email as a parameter, and displays the body of the response
(decoded in utf-8)
"""

import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    var = urllib.parse.urlencode({'email': email})
    var = var.encode('ascii')

    with urllib.request.urlopen(url, var) as response:
        content = response.read()
        print(content.decode('utf-8'))
