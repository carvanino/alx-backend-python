#!/usr/bin/env python3
"""
Complex types - mixed list
"""

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """ Takes in a list of mix integers and floats and returns their sum
    as float """
    sum = 0
    for num in mxd_list:
        sum += num
    return sum
