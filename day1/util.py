#!/usr/bin/env python3

from itertools import tee
# from itertools import pairwise

def pairwise(iterable):
    """Copied from itertools (python3.9 doesn't have pairwise built-in)
    s -> (s0,s1), (s1,s2), (s2, s3), ..."""

    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def triplewise(iterable):
    """Copied from itertools
    Return overlapping triplets from an iterable
    triplewise('ABCDEFG') -> ABC BCD CDE DEF EFG"""

    for (a, _), (b, c) in pairwise(pairwise(iterable)):
        yield a, b, c
