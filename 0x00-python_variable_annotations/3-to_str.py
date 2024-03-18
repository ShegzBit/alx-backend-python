#!/usr/bin/python3
"""A module containing a method that takes a float and returns the string
representation"""


def to_str(n: float) -> str:
    """Takes a float number and returns the string representation of it"""
    return str(n)


if __name__ == "__main__":
    pi_str = to_str(3.14)
    print(pi_str == str(3.14))
    print(to_str.__annotations__)
    print("to_str(3.14) returns {} which is a {}".format(pi_str, type(pi_str)))
