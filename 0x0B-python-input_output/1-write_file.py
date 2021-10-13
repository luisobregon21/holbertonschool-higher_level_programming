#!/usr/bin/python3
''' has function that writes a string '''


def write_file(filename="", text=""):
    ''' writes a string to a text file (UTF8)
        and returns the number of characters written '''
    with open(filename, 'w', encoding='utf-8') as wfile:
        return wfile.write(text)
