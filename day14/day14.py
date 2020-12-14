#!/usr/bin/python3
from math import sin, cos, radians
from collections import namedtuple, defaultdict
from functools import reduce
from itertools import permutations, combinations

lines = open("day14.dat").read().splitlines()

#registers for part 1 and 2
reg1 = {}
reg2 = {}

for line in lines:
    if line.count("mask = ") == 1:
        mask = line.split("mask = ")[1]
        # and mask (to set to 0)
        a = 0
        # or mask (to set to 1)
        o = 0
        # x mask for part 2
        mx = []

        val = 1
        bitcount = 0
        for m in mask[::-1]:
            if (m == "X"):
                mx.append(bitcount)
            if (m != "0"):
                a += val
            if (m == "1"):
                o += val

            val *= 2
            bitcount += 1
    else:
        pos = int(line.split("mem[")[1].split("]")[0])
        val = int(line.split(" = ")[1])

        # write part 1
        reg1[pos] = (val | o) & a

        # basis pos for part 2
        pos = pos | o & a

        # calculate all positions for part 2
        positions = []
        for bit in mx:
            np = set()
            for op in positions:
                np.add(op | (1<<(bit)))
                np.add(op & ~(1<<(bit)))

            np.add(pos | (1<<(bit)))
            np.add(pos & ~(1<<(bit)))

            positions = np

        # write positions for part 2
        for op in positions:
            reg2[op] = val

ans1 = 0
for r in reg1.keys():
    ans1 += reg1[r]

print("Part1:", ans1)

ans2 = 0
for r in reg2.keys():
    ans2 += reg2[r]

print("Part2:", ans2)


