#!/usr/bin/python3
''' Module has a function  that reads a text file '''


def read_file(filename=""):
    ''' reads a text file (UTF8) and prints it to stdout '''
    with open(filename, encoding="utf-8") as rfile:
        for line in rfile:
            print(line, end="")
