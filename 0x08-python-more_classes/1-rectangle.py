#!/usr/bin/python3
''' Module contains an rectangle class '''


class Rectangle:
    ''' Class defines a rectangle '''
    __width = None
    __height = None

    def __init__(self, width=0, height=0):
        ''' init initializes y prende the first instance of the class. '''
        self.height = height
        self.width = width

    @property
    def width(self):
        ''' width getter'''
        return self.__width

    @width.setter
    def width(self, value):
        """ function to set value to self.__width """
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        ''' height getter '''
        return self.__height

    @height.setter
    def height(self, value):
        ''' height setter '''
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
