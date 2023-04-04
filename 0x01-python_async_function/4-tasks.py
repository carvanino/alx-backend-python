#!/usr/bin/env python3
"""
Tasks implementation
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random coroutine n times with a delay of max_delay
    """

    # task_wait_random already return a task object so its okay to do this
    # instead of task = [create_task(task_wait_random(max_delay)) for i in ...]
    task = [await (task_wait_random(max_delay)) for i in range(n)]
    # result = await asyncio.gather(*task)
    return sorted(task)
