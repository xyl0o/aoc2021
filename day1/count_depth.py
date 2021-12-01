#!/usr/bin/env python3

import sys
from util import pairwise, triplewise


def pairwise_incr_count(depths):
    return sum(x < y for x, y in pairwise(depths))


def main():
    with open(sys.argv[1]) as f:
        depths = [int(l) for l in f.read().splitlines()]

    print(pairwise_incr_count(depths))
    print(pairwise_incr_count(sum(t) for t in triplewise(depths)))


if __name__ == '__main__':
    main()
