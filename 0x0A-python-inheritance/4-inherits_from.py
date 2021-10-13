#!/usr/bin/python3
''' Module has function that checks for the instance of a class '''


def inherits_from(obj, a_class):
    ''' return True/False if obj is instance of a class
        that inhereted specified class '''

    if type(obj) == a_class or isinstance(obj, a_class) is False:
        return False
    return True
