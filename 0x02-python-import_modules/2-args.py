#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv
    leng = len(argv) - 1

    if leng == 0:
        print("{:d} arguments.".format(leng))
    elif leng == 1:
        print("{:d} argument:".format(leng))
        print("{:d}: {}".format(leng, argv[1]))
    else:
        print("{:d} arguments:".format(leng))
        for num in range(1, leng + 1):
            print("{:d}: {}".format(num, argv[num]))
