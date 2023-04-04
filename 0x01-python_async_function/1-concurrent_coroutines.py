#!/usr/bin/env python3
"""
Multiple coroutines with async
"""

# import wait_random from './0-basic_async_syntax'
import asyncio
from typing import TYPE_CHECKING, List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Spawns wait_random coroutine n times with a delay of max_delay """
    '''
    delays = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)
    delays = sorted(delays)
    return delays
    '''
    task = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    # task = [wait_random(10), ...]

    result = await asyncio.gather(*task)
    # return task # This returned the tasks objects
    return sorted(result)
