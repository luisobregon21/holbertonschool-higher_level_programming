#!/usr/bin/python3
''' Module has a function that prints names '''


def say_my_name(first_name, last_name=""):
    ''' Function prints first and last name

        param:
        first_name: string that is first name
        last_name: string that is last name
    '''

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
