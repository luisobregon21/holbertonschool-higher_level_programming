#!/usr/bin/python3
''' adds all arguments to a Python list
    and then save them to a file '''

import json
from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

pythonlist = []
jasonfile = "add_item.json"


try:
    pythonlist = load_from_json_file(jasonfile)
except:
    pass
for a in range(1, len(argv)):
    pythonlist.append(argv[a])

save_to_json_file(pythonlist, jasonfile)
