#!/usr/bin/python3
from itertools import combinations
from copy import deepcopy

lines = open("day24.dat").read().splitlines()

def calc(line):
  movements = { "ne": (0.5, 0.5), "se": (0.5, -0.5), "sw": (-0.5, -0.5),
              "nw": (-0.5,0.5), "w": (-1.0, 0.0), "e": (1.0, 0.0) }
  coord = (0.0, 0.0)
  i = 0
  while i < len(line):
    d = line[i]
    if len(line) > i +1:
      d += line[i+1]
      i+=1
    i += 1

    if d in ["ne", "se", "sw", "nw", "e", "w"]:
      pass
    else:
      d = d[0]
      i -= 1

    if d in movements.keys():
      coord = (coord[0] + movements[d][0], coord[1] + movements[d][1])
    else:
      print(d)
      assert(0)

  return coord

def getBlackNei(x,y):
  global pos
  ans = 0
  tocheck = [(x+1,y),(x-1,y),(x+0.5,y+0.5),\
    (x+0.5,y-0.5), (x-0.5,y-0.5), (x-0.5,y+0.5)]
  for to in tocheck:
    if to in pos:
      ans += 1

  return ans

def getNei():
  global pos
  nei = set()
  for i in pos:
    x = i[0]
    y = i[1]
    tocheck = [(x+1,y),(x-1,y),(x+0.5,y+0.5),\
    (x+0.5,y-0.5), (x-0.5,y-0.5), (x-0.5,y+0.5)]
    for to in tocheck:
      if to not in pos:
        nei.add(to)

  return nei

def move():
  new = set()
  for i in pos:
    count = getBlackNei(i[0],i[1])
    if not ((count == 0) | (count > 2)):
      new.add(i)

  nei = getNei()
  for n in nei:
    count = getBlackNei(n[0], n[1])
    if count == 2:
      new.add(n)
  
  return new


pos = set()
for line in lines:
  p = calc(line)
  if p in pos:
    pos.remove(p)
  else:
    pos.add(p)

print("Part1:", len(pos))

for i in range(100):
  pos = move()

print("Part2:", len(pos))


