#!/usr/bin/python3
''' Module has a student class '''


class Student:
    ''' student class '''
    def __init__(self, first_name, last_name, age):
        ''' Instantiation '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        ''' retrieves a dictionary
            representation of a Student instance '''
        return self.__dict__
