#!/usr/bin/python3
for num in range(9):
    for num2 in range(1, 10):
        if num < num2:
            print("{:d}{:d}".format(num, num2), end='')
            if num != 8 or num2 != 9:
                print(", ", end='')
            else:
                print('')
