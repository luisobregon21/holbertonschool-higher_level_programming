#!/usr/bin/python3
for a in range(122, 96, -2):
    print("{}{}".format(chr(a), chr((a-1) - 32)), end='')
