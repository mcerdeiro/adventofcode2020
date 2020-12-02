#!/usr/bin/python3
import itertools
from functools import reduce
from collections import defaultdict

lines = open("day02.dat", "r").read().splitlines()

count1 = 0
count2 = 0
for line in lines:
  data = line.split(" ")
  mi, ma = [int(x) for x in data[0].split("-")]
  let = data[1].split(":")[0]
  pas = data[2]
  co = pas.count(let)
  
  count1 += 1 if ((co >= mi) & (co <= ma)) else 0
  count2 += 1 if (pas[mi-1] == let) ^ (pas[ma-1] == let) else 0

print ("Part1: " + str(count1))
print ("Part2: " + str(count2))

