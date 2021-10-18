#!/usr/bin/python3
''' Module has a Rectangle class '''

from models.base import Base


class Rectangle(Base):
    ''' Rectangle class inherits from Base class'''
    def __init__(self, width, height, x=0, y=0, id=None):
        ''' Class constructor '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        ''' width getter '''
        return self.__width

    @width.setter
    def width(self, value):
        ''' width setter '''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        ''' height getter '''
        return self.__height

    @height.setter
    def height(self, value):
        ''' height setter '''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        ''' x getter '''
        return self.__x

    @x.setter
    def x(self, value):
        ''' x setter '''
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        ''' y getter '''
        return self.__y

    @y.setter
    def y(self, value):
        ''' y setter '''
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        ''' Public method returns the area '''
        return self.width * self.height

    def display(self):
        ''' prints the rectangle in #'s '''
        for newline in range(self.y):
            print()

        for row in range(self.height):
            for space in range(self.x):
                print(" ", end="")
            for column in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        ''' returns: [Rectangle] (<id>) <x>/<y> - <width>/<height> '''
        s = '[Rectangle] ({}) {}/{} - {}/{}'
        return s.format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        ''' assigns arguements to each attribute '''
        if len(args) > 0:
            for a in range(len(args[:5])):
                if a == 0:
                    self.id = args[a]
                if a == 1:
                    self.width = args[a]
                if a == 2:
                    self.height = args[a]
                if a == 3:
                    self.x = args[a]
                if a == 4:
                    self.y = args[a]
        else:
            for key, value in kwargs.items():
                if key == 'width':
                    self.width = value
                if key == 'height':
                    self.height = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value
                if key == 'id':
                    self.id = value

    def to_dictionary(self):
        ''' returns the dictionary representation of a Rectangle '''
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
