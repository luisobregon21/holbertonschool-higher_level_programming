#!/usr/bin/python3
""" Module contains class square """


class Square:
    """ Class defines a square

        Attributes:
            Size is a private instance attribute
            position is a private instance attribute
    """
    __size = None
    __position = None

    def __init__(self, size=0, position=(0, 0)):
        """ init initializes y prende the first instance of the class.
        Args:
            size: is none if no size is passed
        """
        self.__size = size
        self.__position = position

    @property
    def position(self):
        """ function gets the value of the position """
        return self.__position

    @position.setter
    def position(self, value):
        """ function to set value of __position """
        if type(value) is not int and value < (0, 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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
            if (self.__position[1] <= 0):
                for space in range(self.__position[0]):
                    print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()
