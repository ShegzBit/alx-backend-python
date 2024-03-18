#!/usr/bin/env python3
"""This module contains an async routine called wait_n that takes in 2 int
arguments (in this order): n and max_delay. You will spawn wait_random n times
with the specified max_delay.
wait_n should return the list of all the delays (float values). The list of the
delays should be in ascending order without using sort() because of concurrency."""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """Gathers wait_random n times"""
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    result = []
    for task in tasks:
        result += await task
    return result


if __name__ == "__main__":
    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))