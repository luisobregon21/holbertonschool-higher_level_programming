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
        self.__size = size

    @property
    def size(self):
        """ function to get value of __size """
        return self.__size

    @size.setter
    def size(self, value):
        """ function to set value to self.__size """
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ area is a public method that returns the square area """
        return self.__size * self.__size

    def my_print(self):
        """ function prints in stdout the square with the # """
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
