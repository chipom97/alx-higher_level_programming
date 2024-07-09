#!/usr/bin/python3

def multiple_returns(sentence):
    """function that returns a tuple with the
length of a string and its first character."""

    length = 0
    for i in range(len(sentence)):
        length += 1
    return length, sentence[0]
