#!/usr/bin/env python3
"""
Parallel comprehension using asyncio.gather
"""


import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Returns the time it takes for the async_comprehension to be
    executed 4 times
    """
    start = time.perf_counter()
    task = [asyncio.create_task(async_comprehension()) for i in range(4)]
    result = await asyncio.gather(*task)
    total_time = time.perf_counter() - start
    return total_time
