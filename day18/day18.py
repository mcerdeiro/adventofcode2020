#!/usr/bin/python3
lines = open("day18.dat").read().splitlines()

def isNumber(val):
    try:
        int(val)
        return True
    except:
        return False

def process(vals):
    i = 0
    perform = True
    while i < len(vals):
        if vals[i] in ["+", "*"]:
            if isNumber(vals[i-1]) & isNumber(vals[i+1]):
                if ")" in vals:
                    if vals.index(")") < i:
                        perform = False
                if perform:
                    if vals[i] == "+":
                        tmp = int(vals[i-1]) + int(vals[i+1])
                    else:
                        tmp = int(vals[i-1]) * int(vals[i+1])
                    vals.pop(i+1)
                    vals[i] = str(tmp)
                    vals.pop(i-1)
                    i -= 2
                else:
                    perform = True
        i += 1

def processSum(vals):
    i = 0
    while i < len(vals):
        if (vals[i] == "+"):
            if isNumber(vals[i-1]) & isNumber(vals[i+1]):
                tmp = int(vals[i-1]) + int(vals[i+1])
                vals.pop(i+1)
                vals[i] = str(tmp)
                vals.pop(i-1)
                i -= 2
                done = True
        i += 1


def processMul(vals):
    i = 0

    avoid = False
    while i < len(vals):
        if vals[i] == "*":
            if isNumber(vals[i-1]) & isNumber(vals[i+1]):
                if i-2 > 0:
                    if vals[i-2] in ["+"]:
                        avoid = True
                if i+2 < len(vals):
                    if vals[i+2] in ["+"]:
                        avoid = True
                if avoid == False:
                    tmp = int(vals[i-1]) * int(vals[i+1])
                    vals.pop(i+1)
                    vals[i] = str(tmp)
                    vals.pop(i-1)
                    i -= 2
                else:
                    avoid = False
        i += 1

def removePars(vals):
    i = 0
    lastpar = 0
    while i < len(vals):
        if vals[i] == "(":
            lastpar = i
        if vals[i] == ")":
            vals.pop(i)
            vals.pop(lastpar)
            break
        i += 1

def summ1(vals):
    while len(vals) > 1:
        process(vals)
        removePars(vals)
    
    return int(vals[0])

def summ2(vals):
    while len(vals) > 1:
        processSum(vals)
        processMul(vals)
        removePars(vals)
    return int(vals[0])


ans1 = 0
ans2 = 0
for line in lines:
    vals = line.replace("(", " ( ").replace(")"," ) ").split()
    ans1 += summ1(vals[:])
    ans2 += summ2(vals)

print("Part1", ans1)
print("Part2", ans2)
