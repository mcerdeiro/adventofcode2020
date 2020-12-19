#!/usr/bin/python3
from collections import defaultdict
from functools import lru_cache

file = open("day08.dat").read().splitlines()

def run(lines):
    ip = 0
    acc = 0
    ips = []
    finish = False
    
    while finish == False:
        if ip >= len(lines):
            return acc
        if ip in ips:
            finish = True
        else:
            ips.append(ip)

            line = lines[ip]
            ins = line.split(" ")[0]
            count = int(line.split(" ")[1])

            if (ins == "acc"):
                acc += count
            if (ins == "jmp"):
                ip += count - 1

            ip += 1
    
    return acc

def solve(part1 = True):
    if part1:
        return run(file)
    else:
        for index in range(len(file)):
            lines = file[:]
            if (lines[index].split(" ")[0] == "nop"):
                lines[index] = lines[index].replace("nop", "jmp")
            elif (lines[index].split(" ")[0] == "jmp"):
                lines[index] = lines[index].replace("jmp", "nop")
            else:
                continue

            tmp = run(lines)
            if tmp != None:
                return tmp

print("Part1:", solve(True))
print("Part2:", solve(False))