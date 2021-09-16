#!/usr/bin/python3
def roman_to_int(roman_string):
    mapping  = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
        }
    min_ = None
    total = 0
    for c in roman_string:
        val = mapping[c]
        if min_ and val > min_:
            total -= min_*2
        else:
            min_ = val
        total += val
    return total
