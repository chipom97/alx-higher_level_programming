#!/usr/bin/python3
for a in range(0, 10):
    for b in range(a+1, 10):
        print("{}{}".format(a, b), end=", ")
        if a == 8 and b == 9:
            print("{}{}".format(a, b))
