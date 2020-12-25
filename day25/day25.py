#!/usr/bin/python3
from itertools import combinations
from copy import deepcopy

inp = [15733400, 6408062]

def calcLoopSize(sb, result):
  val = 1
  loopsize = 1
  while val != result:
    val = (7 * val) % 20201227
    loopsize += 1
  
  return (loopsize-1)

def encripty(sb, ls):
  val = 1
  modval = 20201227
  for i in range(ls):
    val = (val * sb) % modval

  return val

ls1 = calcLoopSize(7, inp[0])
ls2 = calcLoopSize(7, inp[1])

enc1 = encripty(inp[1], ls1)
enc2 = encripty(inp[0], ls2)

assert(enc1 == enc2)
print("Part1:", enc1)
