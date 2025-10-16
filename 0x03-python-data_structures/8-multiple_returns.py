#!/usr/bin/python3

def multiple_returns(sentence):
	"""Returns the length of a string and its first character."""
	if sentence == "":
		return (0, None)

	length = len(sentence)
	first = sentence[0]

	return (length, first)
