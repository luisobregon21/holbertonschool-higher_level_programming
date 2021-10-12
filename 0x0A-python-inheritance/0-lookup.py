#!/usr/bin/python3
''' Module hold function that returns a list '''


def lookup(obj):
    ''' returns list of available attributes and method

        param:
            @obj: the object being passed
    '''
    return list(dir(obj))
