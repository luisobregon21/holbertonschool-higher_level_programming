#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    avg = 0
    total = 0
    for score, i in my_list:
        avg += score * i
        total += i
    return avg / total
