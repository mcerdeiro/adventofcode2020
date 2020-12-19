#!/usr/bin/python3
from collections import defaultdict
from functools import lru_cache
from itertools import combinations
from copy import deepcopy

lines = [list(y) for y in open("day11.dat").read().splitlines()]
new = deepcopy(lines[:])

X = len(lines)
Y = len(lines[0])

def get(x, y):
    global X, Y
    if (y >= 0) & (y < Y):
        if (x >= 0) & (x < X):
            return lines[y][x]
    return "."

def change(x,y,n):
    global new
    new[y][x] = n

def countAdcOld(x,y):
    oc = 0
    check = [(x+1,y), (x-1,y), (x,y+1), (x,y-1), \
            (x+1,y+1), (x+1,y-1), (x-1,y-1), (x-1,y+1)]

    for c in check:
        if (get(c[0], c[1]) == "#"):
            oc +=1
    return oc

def checkRange(x, y):
    if (y >= 0) & (y < len(lines)):
        if (x >= 0) & (x < len(lines[y])):
            return True
    return False

def countAdc(x,y):
    oc = 0
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), \
            (1, 1), (1, -1), (-1,-1), (-1, +1)]
    for d in dirs:
        p = [x, y]
        while checkRange(p[0], p[1]):
            p[0] += d[0]
            p[1] += d[1]
            if get(p[0],p[1]) == "#":
                oc += 1
                break
            if get(p[0],p[1]) == "L":
                break

    return oc
        

def update(part1 = True):
    global lines, new
    OC = 4
    if part1 == False:
        OC = 5

    for y in range(len(lines)):
        for x in range(len(lines[y])):
            seat = lines[y][x]
            if seat in ["L", "#"]:
                oc = None
                if part1:
                    oc = countAdcOld(x,y)
                else:
                    oc = countAdc(x,y)
                if (seat == "L") & (oc == 0):
                    new[y][x] = "#"
                elif (seat == "#") & (oc >= OC):
                    new[y][x] = "L"
    
    lines = deepcopy(new)
   
def pBoard():
    print("***")
    for lane in lines:
        print ("".join(lane))

def solve(part1 = True):
    newcount = 0
    oldcount = None
    while newcount != oldcount:
        update(part1)
        oldcount = newcount
        newcount = 0
        for l in lines:
            newcount += l.count("#")

    return newcount

backup = deepcopy(lines)
print("Part1:", solve())
lines = deepcopy(backup)
print("Part2:", solve(False))