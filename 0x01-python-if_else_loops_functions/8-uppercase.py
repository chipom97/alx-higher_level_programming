#!/usr/bin/python3

def uppercase(str="chipo"):
    new_str = ""
    for i in str:
        if ord(i) in range(97, 123):
            a = ord(i) - 32
            new_str += chr(a)
        else:
            new_str += i
    print(new_str)
    return f"{new_str}"
