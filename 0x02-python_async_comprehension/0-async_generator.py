#!/usr/bin/env python3
"""a coroutine called async_generator that takes no
arguments. The coroutine will loop 10 times, each time asynchronously
wait 1 second, then yield a random number between 0 and 10. Use
the random module."""
import random
import asyncio


async def async_generator() -> float:
    """An async generator of 10 random values"""
    for i in range(10):
        yield await asyncio.sleep(1, result=random.uniform(0, 10))


if __name__ == "__main__":
    async def print_yielded_values():
        result = []
        async for i in async_generator():
            result.append(i)
        print(result)

    asyncio.run(print_yielded_values())
