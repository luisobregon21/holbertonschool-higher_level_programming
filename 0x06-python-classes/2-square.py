#!/usr/bin/python3
""" Module contains class square """


class Square:
    """ Class defines a square

        Attributes:
            Size is a private instance attribute
    """
    __size = None

    def __init__(self, size=0):
        """ init initializes y prende the first instance of the class.
        Args:
            size: is none if no size is passed
        """
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
