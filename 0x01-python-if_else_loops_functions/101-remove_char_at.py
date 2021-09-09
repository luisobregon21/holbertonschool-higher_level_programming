#!/usr/bin/python3
def remove_char_at(str, n):
    copi = ''
    for index in range(len(str)):
        if index != n:
            copi += str[index]
    return(copi)
