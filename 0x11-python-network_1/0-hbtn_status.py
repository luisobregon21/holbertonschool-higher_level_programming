#!/usr/bin/python3
''' script fetches https://intranet.hbtn.io/status '''

# for opening and reading URLs
import urllib.request


# opens URL
with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    html = response.read()
    r = "Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
    print(r.format(type(html), html, html.decode('utf8')))
