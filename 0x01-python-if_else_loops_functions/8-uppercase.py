#!/usr/bin/python3
def uppercase(str):
    s = ''
    for idx in str:
        if ord(idx) >= 97 and ord(idx) <= 122:
            s += chr(ord(idx) - 32)
        else:
            s += idx
    print("{}".format(s))
