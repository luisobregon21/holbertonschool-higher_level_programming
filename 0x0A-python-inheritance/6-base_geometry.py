#!/usr/bin/python3
''' module holds an empty class '''


class BaseGeometry():
    ''' Has an area method '''
    def area(self):
        ''' public instance method '''
        raise Exception("area() is not implemented")
