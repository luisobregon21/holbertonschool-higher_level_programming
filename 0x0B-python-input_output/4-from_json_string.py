#!/usr/bin/python3
''' Module '''


import json


def from_json_string(my_str):
    ''' returns an object (Python data structure)
    represented by a JSON string: '''
    return json.loads(my_str)
