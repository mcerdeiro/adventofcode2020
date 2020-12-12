#!/usr/bin/python3
from math import sin, cos, radians
from collections import namedtuple

lines = open("day12.dat").read().splitlines()

Position = namedtuple("Position", "x y")
movements = { "N": Position(0, 1), "S": Position(0, -1), "E": Position(1, 0), "W": Position(-1, 0)}

def part1():
    p = Position(0,0)
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
            p = Position(p.x + count * cos(radians(dir)), p.y + count * sin(radians(dir)))
        else:
            p = Position(p.x + movements[move].x * count, p.y + movements[move].y * count)

    return round(abs(p.x)+abs(p.y))

def part2():
    p = Position(0,0)
    dir=0
    way = Position(10, 1)

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
            way = Position(way.x * c - way.y * s, way.x * s + way.y * c)
        elif move == "F":
            p = Position(p.x + way.x * count, p.y + way.y * count)
            
        else:
            way = Position(way.x + movements[move].x * count, way.y + movements[move].y * count)

    return round(abs(p[0])+abs(p[1]))


print("Part1:", part1())
print("Part2:", part2())

