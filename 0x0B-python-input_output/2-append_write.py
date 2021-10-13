#!/usr/bin/python3
''' comment '''


def append_write(filename="", text=""):
    '''  appends a string at the end of a text file (UTF8)
        and returns the number of characters added'''

    with open(filename, 'a', encoding="UTF-8") as afile:
        return afile.write(text)
