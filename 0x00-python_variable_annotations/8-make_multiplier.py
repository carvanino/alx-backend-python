#!/usr/bin/env python3
"""
Complex types - functions
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Takes a float, multiplier as args and returns a callable """
    def float_multiplier(n: float) -> float:
        """ Takes a float as args and return float by multiplier """
        return n * multiplier
    return float_multiplier
