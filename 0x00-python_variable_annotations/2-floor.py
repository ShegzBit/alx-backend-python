#!/usr/bin/env python3
"""
A module containing a floor method that returns math.floor of
a float passed to it
"""
import math


def floor(n: float) -> int:
    """Returns the floor of n"""
    return math.floor(n)


if __name__ == "__main__":
    ans = floor(3.14)

    print(ans == math.floor(3.14))
    print(floor.__annotations__)
    print("floor(3.14) returns {}, which is a {}".format(ans, type(ans)))
