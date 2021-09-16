#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500}
    num = None
    total = 0
    for c in roman_string:
        val = roman[c]
        if num and val > num:
            total -= num * 2
        else:
            num = val
        total += val
    return total
