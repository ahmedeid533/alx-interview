#!/usr/bin/python3
"""Main file for validating"""

def validUTF8(data):
    byte_count = 0

    for item in data:
        if byte_count == 0:
            if item >> 5 == 0b110 or item >> 5 == 0b1110:
                byte_count = 1
            elif item >> 4 == 0b1110:
                byte_count = 2
            elif item >> 3 == 0b11110:
                byte_count = 3
            elif item >> 7 == 0b1:
                return False
        else:
            if item >> 6 != 0b10:
                return False
            byte_count -= 1
    return byte_count == 0
