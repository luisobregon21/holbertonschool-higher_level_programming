#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv
    leng = len(argv)
    total = 0
    if leng - 1 == 0:
        print("0")
    else:
        for num in range(1, leng):
            total += int(argv[num])
        print("{:d}".format(total))
