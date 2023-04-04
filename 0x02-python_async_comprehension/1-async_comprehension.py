#!/usr/bin/env python3
"""
Async Comprehension
"""

import asyncio
from typing import Generator
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None]:
    """
    Collects the yeilded value form async_generator and returns a
    list of all the value
    """
    rand_num = [rand_int async for rand_int in async_generator()]
    return rand_num
'''
    lisN = []
    async for rand_int in async_generator():
        lisN.append(rand_int)
    return lisN
'''
