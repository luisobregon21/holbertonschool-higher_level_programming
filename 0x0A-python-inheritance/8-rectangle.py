#!/usr/bin/python3
''' module holds an empty class '''


class BaseGeometry():
    ''' Has an area method '''
    def area(self):
        ''' public instance method '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        ''' validates the value '''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    ''' class inherits BaseGeometry '''

    def __init__(self, width, height):
        ''' Instantiation '''
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
