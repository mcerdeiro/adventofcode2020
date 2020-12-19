#!/usr/bin/python3
from collections import defaultdict
from functools import lru_cache
from itertools import combinations

lines = open("day10.dat").read().splitlines()
num = [int(x) for x in lines]
copy = num[:]

num = sorted(num)
current = 0
p1 = 0
p3 = 0
px = 0
res = []
while True:
    n2 = filter(lambda x: x < current+4, num)
    n2 = sorted(n2)
    if len(n2) == 0:
        break
    else:
        if n2[0] == current + 1:
            p1 += 1
        elif n2[0] == current + 3:
            p3 += 1
        else:
            px += 1
        current = n2[0]
        num.pop(num.index(n2[0]))

print("Part1:", p1*(p3+1))

ans1 = current+3
num = copy[::-1]
num.append(0)
num = sorted(num)[::-1]

@lru_cache(5)
def ways(i):
    if i == 0:
        return 1

    ans = 0
    tmp = list(filter(lambda x: i > x > i-4, num))
    if len(tmp) == 0:
        return 1

    for t in tmp:
        ans += ways(t)
    
    return ans

print("Part2:", ways(ans1))

