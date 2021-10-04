#!/usr/bin/python3
''' Module contains a rectange class '''


class Rectangle:
    ''' Class defines a rectangle '''
    __width = None
    __height = None
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        ''' init initializes y prende the first instance of the class. '''
        self.height = height
        self.width = width
        type(self).print_symbol = self.print_symbol
        type(self).number_of_instances += 1

    @property
    def width(self):
        ''' width getter'''
        return self.__width

    @width.setter
    def width(self, value):
        """ function to set value to self.__width """
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        ''' height getter '''
        return self.__height

    @height.setter
    def height(self, value):
        '''height setter '''
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        ''' returns the area '''
        return self.__height * self.__width

    def perimeter(self):
        ''' returns perimeter of a rectangle '''
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__height * 2) + (self.width * 2)

    def __str__(self):
        ''' saves element in string '''
        string = ""
        if self.__height == 0 or self.__width == 0:
            return string
        else:
            for row in range(self.__height):
                for column in range(self.__width):
                    string += str(self.print_symbol)
                string += "\n"
            return string[:-1]

    def __repr__(self):
        ''' representation of object '''
        string = "Rectangle"
        string += "(" + str(self.__width) + "," + str(self.__height) + ")"
        return string

    def __del__(self):
        ''' del method '''
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
