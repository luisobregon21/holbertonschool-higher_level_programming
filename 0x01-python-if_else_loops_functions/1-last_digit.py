#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
s = "Last digit of "
if number < 0:
    num = number % -10
else:
    num = number % 10

if num > 5:
    print("{}{:d} is {:d} and is greater than 5".format(s, number, num))
elif num == 0:
    print("{}{:d} is {:d} and is 0".format(s, number, number % 10))
else:
    print("{}{:d} is {:d} and is less than 6 and not 0".format(s, number, num))
