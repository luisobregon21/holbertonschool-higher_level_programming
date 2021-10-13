#!/usr/bin/python3
''' Module has a student class '''


class Student:
    ''' student class '''
    def __init__(self, first_name, last_name, age):
        ''' Instantiation '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        ''' retrieves a dictionary
            representation of a Student instance '''
        if attrs is None:
            return self.__dict__

        dic = {}
        for key in attrs:
            if key in self.__dict__:
                dic[key] = self.__dict__[key]
        return dic
