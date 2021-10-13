#!/usr/bin/python3
''' Module has a class that inherits from int '''


class MyInt(int):
    ''' class inherits from int '''
    def __eq__(self, other):
        ''' reverses __eq__ logic '''
        return (self.real != other.real) or (self.imag != other.imag)

    def __ne__(self, other):
        ''' reverses __ne__ logic '''
        return (self.real == other.real) and (self.imag == other.imag)
