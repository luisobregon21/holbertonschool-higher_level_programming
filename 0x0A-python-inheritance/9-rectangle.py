#!/usr/bin/python3
''' module holds an empty class '''


class BaseGeometry():
    ''' Has an area method '''
    def area(self):
        ''' public instance method '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        ''' validates the value '''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    ''' class inherits BaseGeometry '''
    __width = None
    __height = None

    def __init__(self, width, height):
        ''' Instantiation '''
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        ''' area of rectangle '''
        return self.__width * self.__height

    def __str__(self):
        ''' prints description '''
        return("[Rectangle] {}/{}".format(self.__width, self.__height))
