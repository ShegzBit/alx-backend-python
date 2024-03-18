#!/usr/bin/env python3
"""Creates a task_wait_random sync function"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay):
    """sync wait random function"""
    task = asyncio.create_task(wait_random(max_delay))
    return task
