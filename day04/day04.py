#!/usr/bin/python3
from functools import reduce
from collections import defaultdict
import re

def isNumber(d):
    try:
        tmp = int(d)
    except:
        return False

    return True

def isNumberInRange(d, mi, ma):
    if (isNumber(d)):
        return (mi <= d <= ma)
    else:
        return False

def isHighInRange(high):
    hgt = int(high[0:-2])
    hgtun = high[-2:]
    if (hgtun == "cm"):
        if hgt < 150:
            return False
        if hgt > 193:
            return False
    elif (hgtun == "in"):
        if hgt < 59:
            return False
        if hgt > 76:
            return False
    else:
        return False
    return True

def isHclInRange(hcl):
    if (hcl[0] != "#"):
        return False
    color = hcl[1:]
    if (len(color) != 6):
        return False
    else:
        pattern = r'[^\.0-9a-f]'
        if re.search(pattern, color):
            return False
    return True

lines = open("day04.dat", "r").read().splitlines()
ans1 = 0
ans2 = 0

def check2(d, d2):
    byr = int(d2['byr'])
    if not(isNumberInRange(byr, 1920, 2002)):
        #print("Invalid byr", byr)
        return False
    iyr = int(d2['iyr'])
    if not(isNumberInRange(iyr, 2010, 2020)):
        #print("Invalid iyr", iyr)
        return False
    eyr = int(d2['eyr'])
    if not(isNumberInRange(eyr, 2020, 2030)):
        #print("Invalid eyr", eyr)
        return False
    if not(isHighInRange(d2['hgt'])):
        #print("Invalid hgt", d2['hgt'])
        return False
    if not(isHclInRange(d2['hcl'])):
        #print("Invalid hcl", d2['hcl'])
        return False
    eyecolor = ['amb','blu','brn','gry','grn','hzl','oth']
    if not d2['ecl'] in eyecolor:
        #print("Invalid eyecolor", d2['ecl'])
        return False
    if len(d2['pid']) != 9:
        #print("Invalid pid: ", d2['pid'])
        return False
    if not (isNumber(d2['pid'])):
        #print("Invalid pid", d2['pid'])
        return False
    return True

def part2(d):
    i = ""
    for e in d:
        i += e + " "
    ele = i.split()
    dic = defaultdict(int)
    dic2 = dict()
    for e in ele:
        dic[e.split(":")[0]] += 1
        dic2[e.split(":")[0]] = e.split(":")[1]
    
    if (len(dic) == 8):
        return check2(dic, dic2)
    else:
        if (len(dic) == 7) & (dic['cid'] == 0):
            return check2(dic, dic2)
    return False


def part1(d):
    i = ""
    for e in d:
        i += e + " "
    element = i.split()
    dic = defaultdict(int)
    for e in element:
        dic[e.split(":")[0]] += 1
    
    info = [ 'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    found = True
    for i in info:
        if (dic[i] == 0):
            found = False

    return found


data = []
for line in lines:
    if (line == ""):
        ans1 += part1(data)
        ans2 += part2(data)
        data = []
    else:
        data.append(line)

print ("Part1: " + str(ans1))
print ("Part2: " + str(ans2))

