#!/usr/bin/python3
""" Creates a magic class """


import math


class MagicClass:
    ''' magic class is for a circle '''

    def __init__(self, radius=0):
        ''' initializes '''
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        ''' returns the area '''
        return(self.__radius ** 2 * math.pi)

    def circumference(self):
        ''' returns the circumference '''
        return(2 * math.pi * self.__radius)
