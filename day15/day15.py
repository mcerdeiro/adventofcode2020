#!/usr/bin/python3
from math import sin, cos, radians
from collections import namedtuple, defaultdict
from functools import reduce
from itertools import permutations, combinations

data = [9,12,1,4,17,0,18]

def calc(count):
    index = 0
    I = {}
    prev = None
    prevprev = None

    for i in range(count):
        if i < len(data):
            prev = data[i]
        else:
            if prev in I.keys():
                prev = index-I[prev]-1
            else:
                prev = 0

        I[prevprev] = index - 1
        index += 1
        prevprev = prev

    return prev

print("Part1", calc(2020))
print("Part1", calc(30000000))