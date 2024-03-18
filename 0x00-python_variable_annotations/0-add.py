#!/usr/bin/env python3
"""
A module containing solution to annotated float add function
"""


def add(a: float, b: float) -> float:
    """
    Adds two float and returns their float value
    """
    return a + b


if __name__ == "__main__":
    print(add(1.11, 2.22) == 1.11 + 2.22)
print(add.__annotations__)
