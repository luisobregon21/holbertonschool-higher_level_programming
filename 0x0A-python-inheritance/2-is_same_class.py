#!/usr/bin/python3
''' Module has function that verifies instance '''


def is_same_class(obj, a_class):
    ''' returns True/False if object is exactly an instance
        of a specified class.

        param:
            @obj: object being passed
            @class: specified class
    '''

    if type(obj) == a_class:
        return True
    else:
        return False
