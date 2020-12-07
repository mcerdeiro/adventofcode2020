#!/usr/bin/python3
from collections import defaultdict
from functools import lru_cache

def process(data, l):
    fb = l.split(" bags contain ")[0]
    
    second = l.split(" bags contain ")[1]
    second = second.replace("bags", "bag")
    second = second.replace(".", ",")
    second = second.split(" bag,")
    contains = []
    for s in second:
        if (s!= ""):
            s = s.strip()
            count = s.split(" ")[0]
            if (count == "no"):
                count = 0
            else:
                count = int(count)
            name = " ".join(s.split(" ")[1:])
            name = name.strip()
            contains.append({"count": count, "name": name})

    data[fb] = contains

@lru_cache(512)
def getChilds(bag):
    contains = []
    tmp = data[bag]
    for t in tmp:
        if t["name"] not in contains and t["name"] != "other":
            contains.append(t["name"])
            contains += getChilds(t["name"])
    return contains

@lru_cache(512)
def getContains(bag):
    tmp = data[bag]
    count = 1
    for t in tmp:
        if t["name"] != "other":
            count += t["count"] * getContains(t["name"])

    return count

lines = open("day07.dat").read().splitlines()
data = {}

for line in lines:
    process(data, line)

ans1 = 0
for bag in data.keys():
    contains = getChilds(bag)
    if 'shiny gold' in contains:
        ans1 += 1

print("Part1:",ans1)
print("Part2:", getContains("shiny gold")-1)
