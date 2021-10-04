#!/usr/bin/python3
''' Module has text indentation function '''

def text_indentation(text):
    ''' prints a text with 2 new lines after: ., ?, :

        param:
            text is a string
    '''

    if type(text) is not str:
        raise TypeError("text must be a string")
    else:
        for char in text:
            if char not in [".", "?", ":"]:
                print(char, end="")
            else:
                print("\n")
