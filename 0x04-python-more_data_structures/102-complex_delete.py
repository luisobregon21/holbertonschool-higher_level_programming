#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    holder = a_dictionary.copy()
    for idx, i in holder.items():
        if i == value:
            a_dictionary.pop(idx)
    return a_dictionary
