#!/usr/bin/env python3
"""Duck type an Iterable object"""
from typing import List, Tuple, Iterator, Sequence


def element_length(lst: Iterator[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Returns the value and length of value of the list """
    return [(i, len(i)) for i in lst]
