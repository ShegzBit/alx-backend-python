#!/usr/bin/python3
"""A module containing a function that returns a function that
takes an argument and multiplies it to the argument of this function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """makes a multiplier"""
    def m(n: float) -> float:
        """multiplier to be returned"""
        return n * multiplier
    return m
