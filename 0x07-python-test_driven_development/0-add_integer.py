#!/usr/bin/python3
''' Module  has add integer function '''


def add_integer(a, b=98):
    ''' Function: adds 2 integers
    param:
        a: an 'integer being passed'
        b: 98 if nothing is passed
    '''

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    if type(a) is not int:
        raise TypeError("a must be an integer")
    elif type(b) is not int:
        raise TypeError("b must be an integer")
    else:
        return a + b
