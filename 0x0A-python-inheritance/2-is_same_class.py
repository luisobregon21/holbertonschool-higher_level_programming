#!/usr/bin/python3
''' Module has function that verifies instance '''


def is_same_class(obj, a_class):
    ''' returns True/False if object is exactly an instance
        of a specified class.

        param:
            @obj: object being passed
            @class: specified class
    '''

    return isinstance(obj, a_class)
