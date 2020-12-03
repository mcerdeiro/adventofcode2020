#!/usr/bin/python3
from functools import reduce

lines = open("day03.dat", "r").read().splitlines()

def get(l, p):
  if (p == int(p)):
    p = int(p)
  else:
    return "."
  p = (p % len(l))
  return l[p]

ans1 = 0
ans2 = 0

pos = 0
slope = [1, 3, 5, 7, 0.5]
r = []

for s in slope:
  pos = 0
  ans1 = 0
  for line in lines:
     if (get(line,pos)=="#"):
        ans1 += 1
     pos += s
  r.append(ans1)

ans1 = r[1]
ans2 = reduce(lambda a,b: a*b, r)


print ("Part1: " + str(ans1))
print ("Part2: " + str(ans2))

