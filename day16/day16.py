#!/usr/bin/python3
from math import sin, cos, radians
from collections import namedtuple, defaultdict
from functools import reduce
from itertools import permutations, combinations

lines = open("day16.dat").read().splitlines()

ticketcond = {} # conditions of tickets
yourticket = [] # own ticket
validtickets = [] # valid tickets

def processticketcondition(line):
    typ = line.split(":")[0]
    startrange = line.split(":")[1].split()[0].split("-")
    endrange = line.split(":")[-1].split()[-1].split("-")
    
    return typ, [(int(startrange[0]), int(startrange[1])),\
        (int(endrange[0]),int(endrange[1])) ]

def checkvalue(num):
    for v in ticketcond.values():
        cond = v
        for c in cond:
            if (num >= c[0]) & (num <= c[1]):
                return True
    return False
            
def checkticket(numbers):
    ret = 0
    correct = True
    for num in numbers:
        if checkvalue(num):
            pass
        else:
            ret += num
            correct = False

    return ret, correct

empty = 0
ans1 = 0
for line in lines:
    if line == "":
        empty += 1
        continue

    if empty == 0:
        k, v = processticketcondition(line)
        ticketcond[k] = v
    
    if empty == 1:
        if not line.startswith("your ticket:"):
            yourticket = [int(x) for x in line.split(",")]

    if empty == 2:
        if not line.startswith("nearby tickets:"):
            values = [int(x) for x in line.split(",")]
            ret, correct = checkticket(values)
            if (correct):
                validtickets.append(values)
            else:
                ans1 += ret

print("Part1:", ans1)

def isFieldValid(v, cond):
    for c in cond:
        if (v >= c[0]) & (v <= c[1]):
            return True

    return False

def findkeypos(valtickets, tc):
    keypos = {}
    notfoundkeys = list(tc.keys())
    notfoundcols = [x for x in range(len(validtickets[0]))]

    while len(notfoundcols) > 0:
        posible = {}
        for nf in notfoundkeys:
            posscols = []
            for i in notfoundcols:
                columncorrect = True
                for j in validtickets:
                    if not isFieldValid(j[i], tc[nf]):
                        columncorrect = False
                if (columncorrect):
                    posscols.append(i)
            posible[nf] = posscols
        
        for k,v in posible.items():
            if len(v) == 1:
                keypos[k] = v[0]
                notfoundkeys.remove(k)
                notfoundcols.remove(v[0])

    return keypos

foundpos = findkeypos(validtickets, ticketcond)

ans2 = 1
for key in foundpos.keys():
    if (key.startswith("departure")):
        ans2 *= yourticket[foundpos[key]]

print("Part2:", ans2)

