#!/usr/bin/env python3
"""
Async basics
"""

import asyncio
import random
from typing import TYPE_CHECKING


async def wait_random(max_delay: int = 10) -> float:
    """
    A coroutine that takes an int, max_delay as argument
    and await for a duration of random floating intergers
    between 0 and max_delay
    """
    time = random.uniform(0, 10)
    await asyncio.sleep(time)
    return time
