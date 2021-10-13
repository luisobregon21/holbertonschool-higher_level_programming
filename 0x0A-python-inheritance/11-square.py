#!/usr/bin/python3
''' Module holds class that inherits from rectangle '''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    ''' Class inherits from Rectangle '''
    def __init__(self, size):
        ''' instantiation '''

        super().input_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        ''' prints description '''
        return("[Square] {}/{}".format(self.__size, self.__size))
