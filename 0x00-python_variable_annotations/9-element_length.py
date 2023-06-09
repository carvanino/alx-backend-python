#!/usr/bin/env python3
"""Duck type an Iterable object"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Returns the value and length of value of the list """
    return [(i, len(i)) for i in lst]
