#!/usr/bin/python3
from collections import defaultdict

lines = open("day05.dat", "r").read().splitlines()
ans1 = 0
ans2 = 0
dic = defaultdict(int)

for line in lines:
    row = line[0:7]
    col = line[7:]

    row = row.replace("F","0")
    row = row.replace("B","1")
    row = int(row,2)

    col = col.replace("R","1")
    col = col.replace("L","0")
    col = int(col,2)

    val = row*8+col
    dic[val] += 1
    ans1 = max(val, ans1)

print("Part1: ", ans1)
last = 0
for i in range(1000):
    if (dic[i] == 1) & (dic[i+2] == 1) & (dic[i+1] == 0):
        print("Part2: ", i+1)


