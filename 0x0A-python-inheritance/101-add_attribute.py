#!/usr/bin/python3
''' holds a function '''


def add_attribute(obj, attr, val):
    ''' adds attribute '''
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attr, val)
