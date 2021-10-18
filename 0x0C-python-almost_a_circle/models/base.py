#!/usr/bin/python3
''' Module holds the base class for all other classes '''


import json


class Base:
    ''' manage id attribute in all your future classes
        and to avoid duplicating the same code'''

    __nb_objects = 0

    def __init__(self, id=None):
        ''' The Class constructor:

            Param:
                @self: the instance
                @id: an integer
            '''

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''  returns the JSON string representation of list_dictionaries '''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
