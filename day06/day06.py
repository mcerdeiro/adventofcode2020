#!/usr/bin/python3
from collections import defaultdict

lines = open("day06.dat", "r").read().splitlines()

ans1 = 0
ans2 = 0

part1 = set()
part2 = set()

countlines = 0

for line in lines:
    if (line != ""):
        lineset = set()
        for e in line:
            lineset.add(e)

        part1.update(lineset)

        if countlines == 0:
            part2.update(lineset)
        else:
            part2.intersection_update(lineset)

        countlines += 1

    else:
        ans1 += len(part1)
        ans2 += len(part2)
        part1.clear()
        part2.clear()
        countlines = 0


print("Part1", ans1)
print("Part2", ans2)
