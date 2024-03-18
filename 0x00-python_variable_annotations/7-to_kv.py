#!/usr/bin/env python3
"""A module containing a function that returns a tuple of the args
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple of the k and v^2"""
    return (k, v*v)


if __name__ == "__main__":
    to_kv = __import__('7-to_kv').to_kv

    print(to_kv.__annotations__)
    print(to_kv("eggs", 3))
    print(to_kv("school", 0.02))
