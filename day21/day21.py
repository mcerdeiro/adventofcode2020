#!/usr/bin/python3
from itertools import product
from copy import deepcopy
from itertools import combinations

lines = open("day21.dat").read().splitlines()

R = []
I = set()
A = set()

def processLine(line):
    global I, R, A
    ing = line.split("(")[0].split()
    alerg = line.split("(contains ")[1][0:-1].split(", ")
    R.append((ing,alerg))
    I.update(ing)
    A.update(alerg)

for line in lines:
    processLine(line)

A2I = {}
for r in R:
    for a in r[1]:
        if a in A2I.keys():
            A2I[a].intersection_update(r[0])
        else:
            A2I[a] = set(r[0])

repeat = True
while repeat:
    repeat = False
    for k1,v1 in A2I.items():
        if len(v1) > 1:
            repeat = True
        if len(v1) == 1:
            for k2,v2 in A2I.items():
                if k2 == k1:
                    continue
                tmp = list(v1)[0]
                if tmp in v2:
                    v2.remove(tmp)

IWA = []
for k,v in A2I.items():
    IWA.append(list(v)[0])

ans1 = 0
for v1 in R:
    for v2 in v1[0]:
        if v2 in IWA:
            pass
        else:
            ans1 += 1

print("Part1:", ans1)

I2A = dict()
for k,v in A2I.items():
    I2A[list(v)[0]] = k

IWA = sorted(IWA, key=lambda a: I2A[a])
print("Part2:", ",".join(IWA))
