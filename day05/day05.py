#!/usr/bin/python3
from collections import defaultdict

lines = open("day05.dat", "r").read().splitlines()
ans1 = 0
dic = defaultdict(int)

for line in lines:
    line = line.replace("F","0")
    line = line.replace("B","1")
    line = line.replace("R","1")
    line = line.replace("L","0")
    val = int(line,2)

    dic[val] += 1
    ans1 = max(val, ans1)

print("Part1: ", ans1)
last = 0
for i in range(1000):
    if (dic[i] == 1) & (dic[i+2] == 1) & (dic[i+1] == 0):
        print("Part2: ", i+1)


