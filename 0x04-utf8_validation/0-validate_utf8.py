#!/usr/bin/python3
"""Main file for validating"""

def validUTF8(data):
	for item in data:
		if item & 0b10000000 == 0b10000000:
			return False
	return True
