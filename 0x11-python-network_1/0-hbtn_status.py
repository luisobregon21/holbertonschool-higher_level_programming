#!/usr/bin/python3
''' script fetches https://intranet.hbtn.io/status '''

# for opening and reading URLs
import urllib.request


if __name__ == '__main__':
    # opens URL
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf8')))
