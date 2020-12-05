#!/usr/bin/python3
from collections import defaultdict

lines = open("day05.dat", "r").read().splitlines()
ans2 = []

for line in lines:
    line = "".join(['1' if (x in ["B", "R"]) else '0' for x in line])
    val = int(line,2)
    ans2.append(val)

print("Part1:", max(ans2))

ans2.sort()
for i in range(len(ans2)-1):
    if (ans2[i]+2 == ans2[i+1]):
        print("Part2:", ans2[i]+1)
        exit()


