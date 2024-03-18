#!/usr/bin/python3
"""A module containing a function that adds all ints and floats passed to it
and returns their float result"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of the list of ints and floats"""
    return sum(mxd_lst)
