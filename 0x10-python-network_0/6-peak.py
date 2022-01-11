#!/usr/bin/python3
''' Has a function that finds a peak '''


def find_peak(list_of_integers):
    ''' finds a peak in a list of unsorted integers.'''
    li = list_of_integers
    if len(li) == 0:
        return None
    if len(li) == 1:
        return
    if li[0] >= li[1]:
        return li[0]
    elif li[-1] >= li[-2]:
        return li[-1]
    for idx in range(1, len(li) - 1):
        if li[idx] >= li[idx - 1] and li[idx] >= li[idx + 1]:
            return li[idx]
