#!/usr/bin/env python3
"""
A module containing a type annotated concat function
"""


def concat(str1: str, str2: str) -> str:
    """Adds two str together"""
    return str1 + str2


if __name__ == "__main__":
    str1 = "egg"
    str2 = "shell"
    print(concat(str1, str2) == "{}{}".format(str1, str2))
    print(concat.__annotations__)
