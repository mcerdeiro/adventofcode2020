#!/usr/bin/python3
from copy import deepcopy
from collections import deque

def processInput(lines):
    player = None
    cards = []
    D = {}
    for line in lines:
        if line.startswith("Player "):
            if player != None:
                D[player-1] = cards    
            player = int(line.split()[1][0::-1])
            cards = deque()
        elif (player != None) and (line != ""):
            cards.append(int(line))

    D[player-1] = cards

    return D

def play(d1: deque(), d2: deque(), part1: bool = False):
    sgw = None
    MYD = set()

    while (len(d1) > 0) & (len(d2) > 0):
        tup = tuple([tuple([tuple(d1),"*", tuple(d2)])])
        tup = hash(tup)
        if tup in MYD:
            return 0
        else:
            MYD.add(tup)
        p1 = d1.popleft()
        p2 = d2.popleft()
        if part1 == False:
            if (len(d1) >= p1) & (len(d2) >= p2):
                d1c = deque(list(d1)[0:p1])
                d2c = deque(list(d2)[0:p2])
                sgw = play(d1c, d2c)
            else:
                sgw = None
            
        if (p1 > p2) & (sgw == None) | (sgw == 0):
            d1.append(p1)
            d1.append(p2)
        else:
            d2.append(p2)
            d2.append(p1)
    
    w = 1
    if len(d1) > 0:
        w = 0

    return w

def getScore(D, winner):
    ret = 0
    max = len(D[winner])
    for i in range(len(D[winner])):
        ret += D[winner][i] * max
        max -= 1
    return ret

lines = open("day22.dat").read().splitlines()
D1 = processInput(lines)
D2 = deepcopy(D1)

w = play(D1[0], D1[1], True)
print("Part1:", getScore(D1, w))

w = play(D2[0], D2[1])
print("Part2:", getScore(D2, w))

