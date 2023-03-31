#!/usr/bin/env python3
"""
Type annotations
"""


from typing import Sequence, Any, Union, Mapping, Optional, TypeVar
T = TypeVar('T')


def safely_get_value(
        dct: Mapping, key: Any,
        default: Union[T, None] = None) -> Union[Any, T]:
    """ Duck Types Mapping """
    if key in dct:
        return dct[key]
    else:
        return default
