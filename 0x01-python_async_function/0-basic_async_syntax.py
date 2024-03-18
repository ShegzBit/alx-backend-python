#!/usr/bin/env python3
"""A module containing an asynchronous coroutine that takes in an
integer argument (max_delay, witha default value of 10) named
wait_random that waits for a random delay between 0 and
 max_delay (included and float value) seconds and eventually returns it."""
import random
import asyncio


async def wait_random(max_delay: int =10) -> float:
    """waits for a random number of secs and return the number of secs"""
    result: float = random.uniform(0, 10)
    return await asyncio.sleep(result, result)
