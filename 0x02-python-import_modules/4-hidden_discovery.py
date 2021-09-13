#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    names = dir(hidden_4)
    for num in range(len(names)):
        if names[num][0] != "_":
            print("{}".format(names[num]))
