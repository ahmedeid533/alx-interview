#!/usr/bin/python3
""" minimum operations """


def minOperations(n: int) -> int:
    """ calculate the fewest number of operations """
    if n <= 1:
        return 0
    for i in range(2, n + 1):
        if n % i == 0:
            return minOperations(n // i) + i
    return 0
