#!/usr/bin/python3
from math import sin, cos, radians

lines = open("day12.dat").read().splitlines()

def part1():
    p=[0,0]
    dir = 0
    for line in lines:
        move = line[0]
        count = int(line[1::])
        if move in ["R", "L"]:
            if move == "R":
                dir -= count
            else:
                dir += count
        elif move == "F":
            p[0] += count * cos(radians(dir))
            p[1] += count * sin(radians(dir))
        elif move == "N":
            p[1] += count
        elif move == "S":
            p[1] -= count
        elif move == "E":
            p[0] += count
        elif move == "W":
            p   [0] -= count

    return round(abs(p[0])+abs(p[1]))

def part2():
    p=[0,0]
    dir=0
    way = [10, 1]

    for line in lines:
        move = line[0]
        count = int(line[1::])
        if move in ["R", "L"]:
            if move =="L":
                dir = count
            else:
                dir = -count
            s = sin(radians(dir))
            c = cos(radians(dir))
            way[0], way[1] = [way[0] * c - way[1] * s, way[0] * s + way[1] * c]
        elif move == "F":
            p[0] += way[0]*count
            p[1] += way[1]*count
        elif move == "N":
            way[1] += count
        elif move == "S":
            way[1] -= count
        elif move == "E":
            way[0] += count
        elif move == "W":
            way[0] -= count

    return round(abs(p[0])+abs(p[1]))


print("Part1:", part1())
print("Part2:", part2())

