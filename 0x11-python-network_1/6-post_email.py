#!/usr/bin/python3
"""
Script takes in a URL and an email address, sends a POST request
to the passed URL with the email as a parameter, and
finally displays the body of the response.
"""
from sys import argv
import requests


if __name__ == '__main__':
    response = requests.post(argv[1], data={'email': argv[2]})
    output = response.content.decode('utf8')
    print(output)
