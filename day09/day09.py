#!/usr/bin/python3
from itertools import combinations

lines = open("day09.dat").read().splitlines()
numbers = [int(x) for x in lines]

p1 = 0

for i in range(25, len(numbers), 1):
    comb = combinations(numbers[i-25:i], 2)
    check = False
    for c in comb:
        if sum(c) == numbers[i]:
            check = True
        else:
            pass
    if check == False:
        p1 = numbers[i]
        break

for i in range(len(numbers)):
    part = 0
    mi = 100000000
    ma = 0
    for j in range(i, len(numbers)):
        part += numbers[j]
        ma = max(ma, numbers[j])
        mi = min(mi, numbers[j])
        if (part == p1):
            print("Part1:", p1)
            print("Part2:", mi+ma)
            exit()
        if (part > p1):
            break

