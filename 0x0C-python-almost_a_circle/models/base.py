#!/usr/bin/python3
''' Module holds the base class for all other classes '''


import json
import csv


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

    @classmethod
    def save_to_file(cls, list_objs):
        ''' writes the JSON string representation of list_objs to a file'''
        with open(cls.__name__ + '.json', 'w', encoding='utf-8') as file:
            if list_objs is None:
                file.write("[]")
            else:
                li = []
                for obj in list_objs:
                    li.append(obj.to_dictionary())
                file.write(Base.to_json_string(li))

    @staticmethod
    def from_json_string(json_string):
        ''' returns the list of the JSON string representation json_string '''
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''  that returns an instance with all attributes already set '''
        if cls.__name__ == "Rectangle":
            rec_dummy = cls(1, 1)
            rec_dummy.update(**dictionary)
            return rec_dummy

        if cls.__name__ == "Square":
            sqr_dummy = cls(1)
            sqr_dummy.update(**dictionary)
            return sqr_dummy

    @classmethod
    def load_from_file(cls):
        ''' that returns a list of instances '''
        obj_li = []
        try:
            with open(cls.__name__ + ".json", encoding="utf-8") as f:
                dict_li = Base.from_json_string(f.read())
                for di in dict_li:
                    obj_li.append(cls.create(**di))
                return obj_li
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        ''' seializes in CSV '''
        with open(cls.__name__ + ".csv", mode="w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                li = []
                for obj in list_objs:
                    li.append(obj.to_dictionary())
                if cls.__name__ == "Rectangle":
                    attr = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == "Square":
                    attr = ['id', 'size', 'x', 'y']
                writer = csv.DictWriter(f, fieldnames=attr)
                ''' writing the headers '''
                writer.writeheader()
                for dic in li:
                    ''' writing the rows'''
                    writer.writerow(dic)

    @classmethod
    def load_from_file_csv(cls):
        ''' deserializes in CSV '''
        obj_li = []
        try:
            with open(cls.__name__ + ".csv", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for di in reader:
                    for val in di:
                        di[val] = int(di[val])
                    obj_li.append(cls.create(**di))
                return obj_li
        except IOError:
            return []
