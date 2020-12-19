#!/usr/bin/python3
from itertools import product

lines = open("day19.dat").read().splitlines()
R = {}

def processRule(line):
    rule = int(line.split(":")[0])
    letter = None
    parts = []

    rest = line.split(":")[1]
    if "\"" in rest:
        letter = rest.split("\"")[1][0]
    else:
        for ors in rest.split("|"):
            ands = ors.split()
            tmp = []
            for a in ands:
                tmp.append(int(a))
            parts.append(tmp)

    R[rule] = {"l": letter, "p": parts}


def combinations2(p1 = set(), p2 = set()):
    new = set()
    if len(p1) == 0:
        return p2
    if len(p2) == 0:
        return p1
    
    for p1m in p1:
        for p2m in p2:
            new.add(p1m + p2m)

    assert(len(new) == len(p1) * len(p2))
    return new

def getStrings(r):
    ret = set()

    if R[r]["l"] != None:
        ret.add(R[r]["l"])
        return ret
    else:
        for subr in R[r]["p"][0]:
            r1 = getStrings(subr)
            ret = combinations2(ret, r1)
        if len(R[r]["p"]) == 2:
            new = set()
            for subr in R[r]["p"][1]:
                r1 = getStrings(subr)
                new = combinations2(new, r1)
            ret.update(new)

    return ret
            
def checkPart2(line, rule42, rule31):
    count42 = 0
    newlen = len(line)
    oldlen = 0
    while newlen != oldlen:
        if line[0:8] in rule42:
            line = line[8::]
            count42 += 1
        oldlen = newlen
        newlen = len(line)

    count31 = 0
    newlen = len(line)
    oldlen = 0
    while newlen != oldlen:
        if line[0:8] in rule31:
            line = line[8::]
            count31 += 1
        oldlen = newlen
        newlen = len(line)

    if (count42 > count31) & (count42 > 1) & (count31 > 0) & (len(line) == 0):
        return True

    return False

ans1 = 0
ans2 = 0
empty = 0

for line in lines:
    if line == "":
        empty += 1
        possibleStrings = getStrings(0)
        #for part 2
        possibleStrings42 = getStrings(42)
        possibleStrings31 = getStrings(31)

    if empty == 0:
        processRule(line)

    if empty == 1:
        if line in possibleStrings:
            ans1 += 1
            ans2 += 1
        elif checkPart2(line, possibleStrings42, possibleStrings31):
            ans2 += 1

print("Part1", ans1)
print("Part2", ans2)