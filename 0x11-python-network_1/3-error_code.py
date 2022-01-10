#!/usr/bin/python3
'''
takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).
'''


from sys import argv
from urllib.request import urlopen
from urllib.error import HTTPError


if __name__ == "__main__":
    try:
        with urlopen(argv[1]) as response:
            print(response.read().decode('utf8'))
    except HTTPError as error:
        print("Error code: {}".format(error.code))
