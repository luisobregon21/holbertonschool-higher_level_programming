#!/usr/bin/python3
''' Module holds a Square Class '''


from models.rectangle import Rectangle


class Square(Rectangle):
    ''' class inherits from Rectangle class '''
    def __init__(self, size, x=0, y=0, id=None):
        ''' Class constructor '''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        ''' size getter '''
        return self.width

    @size.setter
    def size(self, value):
        ''' size setter '''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value

    def __str__(self):
        ''' returns: [Square] (<id>) <x>/<y> - <size>'''
        s = '[Square] ({self.id}) {self.x}/{self.y} - {self.width}'
        return s.format(self=self)

    def update(self, *args, **kwargs):
        ''' assigns arguements to each attribute '''
        if len(args) > 0:
            for a in range(len(args[:4])):
                if a == 0:
                    self.id = args[a]
                if a == 1:
                    self.size = args[a]
                if a == 2:
                    self.x = args[a]
                if a == 3:
                    self.y = args[a]
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    self.size = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value
                if key == 'id':
                    self.id = value

    def to_dictionary(self):
        ''' returns the dictionary representation of a Rectangle '''
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
