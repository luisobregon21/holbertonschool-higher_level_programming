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
