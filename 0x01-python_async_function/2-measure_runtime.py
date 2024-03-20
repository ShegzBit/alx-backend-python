#!/usr/bin/env python3
"""a measure_time function with integers n and max_delay as arguments\
that measures thetotal execution time for wait_n(n, max_delay),
and returns total_time / n. Your function should
return a float."""
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Measures time average taken for each task"""
    start = time.perf_counter()
    wait_n(n, max_delay)
    end = time.perf_counter()
    return (end - start) / n


if __name__ == "__main__":
    n = 5
    max_delay = 9

    print(measure_time(n, max_delay))
