#!/usr/bin/python3
"""
Takes in a URL and an email, sends a POST request to the passed URL with the
email as a parameter, and displays the body of the response (decoded in utf-8)
"""
from sys import argv
import urllib.request
import urllib.parse


if __name__ == "__main__":
    url = argv[1]
    data = urllib.parse.urlencode({'email': argv[2]})
    # encondes the data
    data = data.encode('utf8')
    with urllib.request.urlopen(url, data) as response:
        print(response.read().decode('utf8'))
