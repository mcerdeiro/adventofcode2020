#!/usr/bin/python3
from math import sin, cos, radians
from collections import namedtuple
from functools import reduce
from itertools import combinations
from modint import ChineseRemainderConstructor, chinese_remainder

lines = open("day13.dat").read().splitlines()
offset = int(lines[0])
ids_x = [x for x in lines[1].split(",")]
ids = filter(lambda a: a != "x", ids_x)
ids = [int(x) for x in ids]

mintime = 100000000000000
mimbus = 0
for n in ids:
    start = offset//n
    for i in range(10000):
        check = n*(i+start)
        if (check >= offset):
            if (n*(i+start)-offset<mintime):
                mintime = n*(i+start)-offset
                minbus = n
            break

print("Part1", mintime * minbus)

n = []
a = []
for i in ids:
    n.append(i)
    a.append(i-ids_x.index(str(i)))

print("Part2", chinese_remainder(n,a))
