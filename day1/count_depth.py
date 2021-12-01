#!/usr/bin/env python3

import sys

from itertools import tee
# from itertools import pairwise


def pairwise(iterable):
    """Copied from itertools (python3.9 doesn't have pairwise built-in)
    s -> (s0,s1), (s1,s2), (s2, s3), ..."""
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def main():
	with open(sys.argv[1]) as f:
		lines = f.read().splitlines()

	print(sum(x < y for x, y in pairwise(int(l) for l in lines)))


if __name__ == '__main__':
	main()