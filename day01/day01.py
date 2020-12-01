#!/usr/bin/python3
import itertools
from functools import reduce 

lines = open("day01.dat", "r").read().splitlines()
lines = [int(x) for x in lines]

def prod(val):
  return reduce(lambda a,b: a*b, list(val))

for comb in itertools.combinations(lines, 2):
  if (sum(list(comb)) == 2020):
    print("Part1: " + str(prod(comb)))
    break

for comb in itertools.combinations(lines, 3):
  if (sum(list(comb)) == 2020):
    print("Part2: " + str(prod(comb)))
    break