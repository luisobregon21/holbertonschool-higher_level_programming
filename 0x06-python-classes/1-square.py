#!/usr/bin/python3
""" Module contains class square """


class Square:
    """ Class defines a square

        Attributes:
            Size is a private instance attribute
    """
    def __init__(self, size):
        """ init initializes y prende the first instance of the class.
        Args:
            size: is none if no size is passed
        """
        self.__size = size
