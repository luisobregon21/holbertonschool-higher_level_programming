#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv
    leng = len(argv) - 1
    if leng > 1:
       print("{:d} arguements:".format(leng))
       for num in range(1, leng + 1):
           print("{:d}: {}".format(num, argv[num]))
    elif leng == 0:
        print("0 arguements.")
    elif leng == 1:
        print("{1 arguement:".format(leng))
        print("{1: {}".format(argv[1]))
