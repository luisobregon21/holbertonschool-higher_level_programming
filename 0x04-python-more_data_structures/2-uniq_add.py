#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = 0
    uniq = set(my_list)
    for i in uniq:
        add += i
    return add
