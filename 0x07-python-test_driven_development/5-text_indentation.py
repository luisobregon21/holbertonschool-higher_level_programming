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
        space_start = 1
        for char in text:
            if char == " " and space_start == 1:
                continue
            print(char, end="")
            space_start = 0
            if char in [".", "?", ":"]:
                print("\n")
                space_start = 1
