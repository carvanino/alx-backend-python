#!/usr/bin/env python3
"""
Async Generator
"""

import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    A coroutine that loops 10 times and yields a random float between 0, 10
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
