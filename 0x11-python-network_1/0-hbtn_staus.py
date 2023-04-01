#!/usr/bin/python3

import urllib.request

url = "https://alx-intranet.hbtn.io/status"
r = urllib.request.Request(url)

with urllib.request.urlopen(url) as response:
    read_func = response.read()

print("Body response:")
print(f"\t- type: {type(read_func)}")
print(f"\t- content: {read_func}")
print(f"\t- utf-8 content: {read_func.decode('utf-8')}")
