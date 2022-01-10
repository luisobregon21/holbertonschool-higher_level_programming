#!/usr/bin/python3
"""
Script takes in a URL, sends a request to the URL and displays the body
of the response. If the HTTP status code is greater than or equal to 400,
print: Error code: followed by the value of the HTTP status code.
"""
from sys import argv
import requests


if __name__ == '__main__':
    response = requests.get(argv[1])
    status = response.status_code
    if status >= 400:
        print("Error code: {}".format(status))
    else:
        print(response.content.decode('utf8'))
